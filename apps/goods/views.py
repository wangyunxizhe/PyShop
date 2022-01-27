from datetime import date

from apscheduler.schedulers.background import BackgroundScheduler
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
from haystack.views import SearchView

from apps.contents.models import ContentCategory
from apps.goods.models import GoodsCategory, SKU, GoodsVisitCount
from utils.goods import get_categories, get_breadcrumb, get_goods_specs


# from fdfs_client.client import Fdfs_client

# 功能测试代码：使用FastDFS上传图片至服务器
# 1，加载FastDFS客户端
# client = Fdfs_client('utils/fastdfs/client.conf')
# 2，上传图片
# client.upload_by_filename('E:/py-workspaces/pyShop/static/好像一条狗.jpg')
# 3，获取file_id，upload_by_filename上传成功会返回字典数据（其中包含file_id）


class IndexView(View):
    """
    首页-商品分类；跳转首页模板，非直接与前端交互，测试用
    """

    def get(self, request):
        # 获取商品分类数据
        categories = get_categories()
        # 广告数据
        contents = {}
        content_categories = ContentCategory.objects.all()
        for cat in content_categories:
            contents[cat.key] = cat.content_set.filter(status=True).order_by('sequence')

        context = {
            'categories': categories,
            'contents': contents,
        }
        '''
        正常 首页 会使用 页面静态化 渲染，
        这里先把数据都返回给本项目的html模板
        '''
        return render(request, 'index.html', context)


class ListView(View):
    """
    首页-商品分类-商品分类列表跳转展示
    """

    def get(self, request, category_id):
        # 根据商品分类id,进行商品分类数据查询
        try:
            category = GoodsCategory.objects.get(id=category_id)
        except GoodsCategory.DoesNotExist:
            return JsonResponse({'code': 400, 'errMsg': '参数缺失'})
        # 根据查询出的商品分类数据组装"面包屑"数据
        breadcrumb = get_breadcrumb(category)
        # 根据商品分类数据查询对应的SKU数据,并根据传入的字段进行排序
        # 获取前端传入的需要排序的字段
        ordering = request.GET.get('ordering')
        skus = SKU.objects.filter(category=category, is_launched=True).order_by(ordering)
        # 将排序后的skus进行分页
        # 接收前端传入的每页条数
        page_size = request.GET.get('page_size')
        # 接收前端传入的页码
        page = request.GET.get('page')
        paginator = Paginator(skus, per_page=page_size)
        skus_page = paginator.page(page)
        # 将对象转换为字典
        sku_list = []
        for sku in skus_page.object_list:
            sku_list.append({
                'id': sku.id,
                'name': sku.name,
                'price': sku.price,
                'default_image_url': sku.default_image.url
            })
        # 总页码
        total_num = paginator.num_pages
        return JsonResponse({'code': 0, 'errMsg': 'ok', 'list': sku_list, 'count': total_num, 'breadcrumb': breadcrumb})


class HotGoodsView(View):
    """
    首页-商品分类-热销商品
    """

    def get(self, request, category_id):
        # 利用category_id去数据库把该类别的商品按照销量倒序排序，并取出前3条
        skus = SKU.objects.filter(category_id=category_id).order_by('-sales')[:3]

        # 把数据转换成前端想要的格式
        hot_skus = []
        for sku in skus:
            hot_skus.append({
                'id': sku.id,
                'default_image_url': sku.default_image.url,
                'name': sku.name,
                'price': sku.price
            })
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'hot_skus': hot_skus})


class SKUSearchView(SearchView):
    """ES以及Haystack配置完成后的具体使用：首页-商品搜索栏"""

    # 重写 create_response 方法，以便返回JSON格式数据
    def create_response(self):
        # 获取数据搜索的结果
        context = self.get_context()
        sku_list = []
        for sku in context['page'].object_list:
            sku_list.append({
                'id': sku.object.id,
                'name': sku.object.name,
                'price': sku.object.price,
                'default_image_url': sku.object.default_image.url,
                'searchkey': context.get('query'),
                'page_size': context['page'].paginator.num_pages,
                'count': context['page'].paginator.count
            })
        return JsonResponse(sku_list, safe=False)


class DetailView(View):
    """商品详情；跳转详情页模板，非直接与前端交互，测试用"""

    def get(self, request, sku_id):
        try:
            sku = SKU.objects.get(id=sku_id)
        except SKU.DoesNotExist:
            pass
        categories = get_categories()
        # 根据skuID查询出的具体商品，组装"面包屑"数据
        breadcrumb = get_breadcrumb(sku.category)
        # 获取该商品的规格信息
        goods_specs = get_goods_specs(sku)
        context = {
            'categories': categories,
            'breadcrumb': breadcrumb,
            'sku': sku,
            'specs': goods_specs,
        }
        '''
        正常 详情页 会使用 页面静态化 渲染，
        这里先把数据都返回给本项目的html模板
        '''
        return render(request, 'detail.html', context)


class CategoryVisitCountView(View):
    """分类商品统计访问量"""

    def post(self, request, category_id):
        # 根据传入的商品分类id，查询该商品分类
        try:
            category = GoodsCategory.objects.get(id=category_id)
        except GoodsCategory.DoesNotExist:
            return JsonResponse({'code': 400, 'errMsg': '无此商品分类'})
        # 查询当天这个分类的记录
        today = date.today()
        try:
            gvc = GoodsVisitCount.objects.get(category=category, date=today)
        except GoodsVisitCount.DoesNotExist:
            # 无当天数据，新建数据
            GoodsVisitCount.objects.create(category=category, date=today, count=1)
        else:
            # 已有当天数据，更新数据，使访问量+1
            gvc.count += 1
            gvc.save()
        return JsonResponse({'code': 0, 'errmsg': 'ok'})
