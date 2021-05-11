# -*- coding: utf-8 -*-
# @Time    : 2021/5/11
# @Author  : 王渊

from django.urls import path
from book.views import index

# 固定写法：urlpatterns = []
urlpatterns = [
    # 添加路由，指向自己的视图层函数
    path('index/', index),
]
