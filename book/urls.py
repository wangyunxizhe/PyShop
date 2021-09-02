# -*- coding: utf-8 -*-
# @Time    : 2021/5/11
# @Author  : 王渊

from django.urls import path
from book.views import *
from django.urls import converters
from django.urls.converters import register_converter


# 1，定义转换器
class MobileConverter:
    regex = '1[3-9]\\d{9}'

    # 验证通过的数据返回给视图层函数
    def to_python(self, value):
        return value


# 2，转换器要注册后才能使用
register_converter(MobileConverter, 'phone')  # 调用注册方法，并为自定义的转换器起名：phone

# 固定写法：urlpatterns = []
urlpatterns = [
    # 添加路由，指向自己的视图层函数
    path('index/', index),
    path('create/', create),
    # 接收RESTful风格参数（和book/views.py对应看）
    # 参数合法性校验（方式2）, <int:city_id>:<转换器名字:变量名>
    # <phone:mobile>:实现自定义转换器检验手机号的合法性
    path('<int:city_id>/<shop_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', post_json),
    path('method/', method_type),
    path('myJsonResp/', my_json_resp),
    path('myRedirect/', http_redirect),
    path('setMyCookie/', set_my_cookie),
    path('getMyCookie/', get_my_cookie),
]
