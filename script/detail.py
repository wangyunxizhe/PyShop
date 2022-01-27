import time
from apps.goods.models import SKU
from utils.goods import get_categories, get_breadcrumb, get_goods_specs
import sys
import os
import django
from django.template import loader
"""
独立运行的py脚本，用于生成所有商品的详情页
运行方式：要在pycharm Edit Configurations中勾选run with python console，然后以Run方式运行
"""

# 目标路径base_dir
sys.path.insert(0, '../')
# 告诉 os django的配置文件在哪里
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyShop.settings")
# 相当于 当前的文件 有了django的环境
django.setup()


def generic_shop_detail(sku):
    """
    页面静态化：针对本项目的详情页
    与首页不同点：内容变化比较少，一般就是有活动时价格会变动。应该在上线时统一生成一遍
    """
    print('--------------%s:开始生成detail.html-------------' % time.ctime())
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
    # 加载需要渲染的模板
    detail_template = loader.get_template('detail.html')
    # 把后台查询到的数据给模板
    detail_html_data = detail_template.render(context)
    # 把渲染后的各个商品的详情页面，写入到指定的前端文件夹中
    file_path = os.path.join('E:/VScode--workspace/pyShop/front_end_pc/goods/%s.html' % sku.id)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(detail_html_data)
    print('--------------已生成%s.html-------------' % sku.id)


skus = SKU.objects.all()
for sku in skus:
    generic_shop_detail(sku)
