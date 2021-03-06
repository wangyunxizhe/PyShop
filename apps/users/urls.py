from django.urls import path

from apps.users.views import *

urlpatterns = [
    # RESTful接口，判断用户名是否重复，使用自定义转换器（转换器位置：E:\py-workspaces\pyShop\utils\converters.py）
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('info/', CenterView.as_view()),
    path('emails/', EmailView.as_view()),
    path('emails/verification/', EmailVerifyView.as_view()),
    path('addresses/create/', AddressCreateView.as_view()),
    path('addresses/', AddressView.as_view()),
]
