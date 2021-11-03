"""pyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from utils.converters import UsernameConverter
from django.urls import register_converter

# 注册转换器
register_converter(UsernameConverter, 'username')

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加子应用的路由：
    # 引入子应用（book）中的urls.py
    path('', include('book.urls')),
    # 引入子应用（users）中的urls.py
    path('', include('apps.users.urls')),
]
