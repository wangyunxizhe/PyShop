from django.urls import path

from apps.users.views import UsernameCountView

urlpatterns = [
    # RESTful接口，判断用户名是否重复，使用自定义转换器（转换器位置：E:\py-workspaces\pyShop\utils\converters.py）
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
]
