from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse, JsonResponse
import json
import re

# Create your views here.
from django.views import View

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


######################Cookie+Session######################
"""
Cookie
第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?username=wyuan&password=123
服务器接收到请求之后，获取username，服务器设置cookie信息，cookie信息中包含username
浏览器接收到服务器响应之后，应该把cookie保存起来

第二次及其之后的请求，我们访问 http://127.0.0.1:8000/，都会携带cookie信息，
服务器就可以读取cookie信息，来判断用户身份
"""


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


"""
Session
session是保存在服务器端，需要依赖于cookie

第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_session/?username=ironman，在服务器端设置session信息，
服务器同时会生成一个sessionid的cookie信息。浏览器接收到这个信息后，会把cookie数据保存起来。

第二次及其之后的请求，都会携带这个sessionid，服务器会去验证这个sessionid，
验证没有问题会读取相关数据，实现业务逻辑
"""


def set_my_session(request):
    # 1，获取GET请求中的username信息
    username = request.GET.get('username')
    # 2 设置session（同时Django框架也将该数据落库进了 django_session 表中）
    request.session['username'] = username

    # 也可以给session设置过期时间，单位是秒
    request.session.set_expiry(360)
    # clear：删除session里的数据，但是会保留key
    # request.session.clear()
    # flush：删除所有的数据，包括key
    # request.session.flush()

    return HttpResponse('set_my_session')


def get_my_session(request):
    username = request.session.get('username')
    content = '{}'.format(username)
    return HttpResponse(content)


######################类视图######################
# 在Django中也可以使用类来定义一个视图，称为类视图

def login(request):
    if request.method == 'GET':
        return HttpResponse('Get 请求')
    else:
        return HttpResponse('Post 请求')


"""
类视图的定义:
1，要继承View类。
2，类视图中的方法名是采用http方法的小写，用于区分前端不同的请求方式
例：
class 类视图名字（View）:
    def get(self,request):
        return HttpResponse('xxx')
    def http_method_lower(self,request):
        return HttpResponse('xxx')
"""


class LoginView(View):

    def get(self, request):
        return HttpResponse('get 类视图 get')

    def post(self, request):
        return HttpResponse('post 类视图 post')
