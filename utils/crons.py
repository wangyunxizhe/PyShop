import os
import time

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

from utils.goods import get_categories
from apps.contents.models import ContentCategory
from django.template import loader

"""
定时任务类：django-crontab配置见settings.py（只支持Linux系统，Windows系统不适用）
"""


def generic_shop_index():
    """
    页面静态化：针对本项目的首页，详情页面
    目的：让用户可以直接访问经过数据渲染后的html，不用在访问的同时等待后台数据的返回
    做法：将已经经过数据渲染的html写入到指定的前端目录中
    """
    print('--------------%s:开始生成index.html-------------' % time.ctime())
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
    # 加载需要渲染的模板
    index_template = loader.get_template('index.html')
    # 把后台查询到的数据给模板
    index_html_data = index_template.render(context)
    # 把渲染后的HTML，写入到指定的前端html文件
    file_path = os.path.join('E:/VScode--workspace/pyShop/front_end_pc/index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(index_html_data)

