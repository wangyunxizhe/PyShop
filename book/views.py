from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
"""
视图层相关代码
视图层函数的2个要求：
1，第一个参数就是 接受请求，这个请求就是 HttpRequest 的类对象。
2，必须 return 一个响应
"""


def index(request):
    # render函数的作用：渲染视图
    return render(request, 'book/index.html')
