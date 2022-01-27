from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import path
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

from apps.goods.views import IndexView, ListView, HotGoodsView, SKUSearchView, DetailView, CategoryVisitCountView
from apps.users.views import *
from utils.crons import generic_shop_index

urlpatterns = [
    path('index/', IndexView.as_view()),
    path('list/<category_id>/skus/', ListView.as_view()),
    path('hot/<category_id>/', HotGoodsView.as_view()),
    path('search/', SKUSearchView()),
    path('detail/<sku_id>/', DetailView.as_view()),
    path('detail/visit/<category_id>/', CategoryVisitCountView.as_view()),
]

# 开启django-apscheduler定时工作
# 若数据库已有定时任务的记录，注释掉 add 的部分
try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    # scheduler.add_jobstore(DjangoJobStore(), "default")
    # 间隔1分钟，执行generic_shop_index方法，以生成渲染后的首页html
    # 方式一
    # scheduler.add_job(generic_shop_index, 'interval', seconds=60, id='index_job')
    # 方式二
    # @register_job(scheduler, "interval", seconds=60, id='index_job')
    # def index_job():
    #     generic_shop_index()
    # register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()
