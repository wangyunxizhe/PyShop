from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import path
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

from apps.goods.views import IndexView, ListView, HotGoodsView, SKUSearchView, DetailView
from apps.users.views import *
from utils.crons import generic_shop_index

urlpatterns = [
    path('index/', IndexView.as_view()),
    path('list/<category_id>/skus/', ListView.as_view()),
    path('hot/<category_id>/', HotGoodsView.as_view()),
    path('search/', SKUSearchView()),
    path('detail/<sku_id>/', DetailView.as_view()),
]

# 开启django-apscheduler定时工作
try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # 间隔1分钟，执行generic_shop_index方法，以生成渲染后的首页html
    @register_job(scheduler, "interval", seconds=60, id='index_job')
    def index_job():
        generic_shop_index()


    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()
