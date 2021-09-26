from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse, JsonResponse
import json
import re

# Create your views here.
from book.models import BookInfo

"""
视图层相关代码

视图层函数的2个要求：
1，第一个参数就是 接受请求，这个请求就是 HttpRequest 的类对象。
2，必须 return 一个响应
"""


def index(request):
    # render函数的作用：渲染视图
    return render(request, 'book/index.html')


def create(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2021-5-12',
        read_count=10
    )
    return HttpResponse("create")


# 接收RESTful风格参数（和book/urls.py对应看）
def shop(request, city_id, shop_id, mobile):
    # 校验参数合法性：方式1（方式2见book/urls.py）
    if not re.match("\\d{5}", shop_id):
        return HttpResponse('没有此 shop_id')
    return HttpResponse("city_id:" + str(city_id) + " shop_id:" + shop_id + " mobile:" + mobile)


# 接收POST请求--表单数据
def register(request):
    data = request.POST
    print(data)
    return HttpResponse("POST form-data")


# 接收POST请求--JSON数据
def post_json(request):
    body = request.body
    print(body)
    body_str = body.decode()
    print("str:{}".format(body_str))
    # json.loads将JSON字符串转换为字典
    body_dict = json.loads(body_str)
    print("dict:{}".format(body_dict))
    print("请求头--端口号：{}".format(request.META('SERVER_PORT')))
    return HttpResponse("POST json")


def method_type(request):
    m_type = request.method
    return HttpResponse("请求类型：{}".format(m_type))


# 向前端返回json数据
def my_json_resp(request):
    info = {
        'name': 'wyuan',
        'add': 'NJ'
    }
    infos = [{
        'name': 'wyuan',
        'add': 'NJ'
    }, {
        'name': 'xiaom',
        'add': 'SH'
    }]
    '''
    safe=True 表示 data中传递的是 字典类型 的数据，JsonResponse可以把字典转换为JSON。
    若要传 非字典数据 到前端，需要将 safe=False
    '''
    my_resp = JsonResponse(data=info, safe=False)
    return my_resp


# 重定向
def http_redirect(request):
    return redirect('http://www.baidu.com')


#######################################Cookie和Session#######################################

def set_my_cookie(request):
    # 1，获取GET请求中的username信息
    username = request.GET.get('username')
    addr = request.GET.get('addr')
    # 2，在服务器设置cookie的信息
    response = HttpResponse('set_my_cookie')
    response.set_cookie("name", username)
    # 可以设置cookie的过期时间，单位是秒
    response.set_cookie("addr", addr, max_age=60)
    return response


def get_my_cookie(request):
    print(request.COOKIES)
    # 获取服务器中的cookie指定信息（cookie是dict类型数据）
    name = request.COOKIES.get('name')
    return HttpResponse(name)


def set_my_session(request):
    # 1，获取GET请求中的username信息
    username = request.GET.get('username')
    # 2 设置session（同时Django框架也将该数据落库进了 django_session 表中）
    request.session['username'] = username
    return HttpResponse('set_my_session')


def get_my_session(request):
    username = request.session.get('username')
    content = '{}'.format(username)
    return HttpResponse(content)
