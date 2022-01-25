from django.urls import path

from apps.goods.views import IndexView
from apps.users.views import *

urlpatterns = [
    path('goods_index/', IndexView.as_view()),
]
