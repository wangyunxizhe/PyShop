from django.shortcuts import render
from django.views import View

from apps.contents.models import ContentCategory
from utils.goods import get_categories


# from fdfs_client.client import Fdfs_client

# 功能测试代码：使用FastDFS上传图片至服务器
# 1，加载FastDFS客户端
# client = Fdfs_client('utils/fastdfs/client.conf')
# 2，上传图片
# client.upload_by_filename('E:/py-workspaces/pyShop/static/好像一条狗.jpg')
# 3，获取file_id，upload_by_filename上传成功会返回字典数据（其中包含file_id）


class IndexView(View):

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
