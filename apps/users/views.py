import json
import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from apps.users.models import User, Address
from apps.users.utils import generic_email_verify_token, check_verify_token
from celery_tasks.email.tasks import celery_send_email
from pyShop import settings


class UsernameCountView(View):

    def get(self, request, username):
        # 以下操作使用 utils/converters.py 中的自定义转换器来完成
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 200, 'errMsg': '用户名不符合要求'})
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 200, 'count': count, 'errMsg': 'OK'})


class RegisterView(View):
    '''
    注册请求
    '''

    def post(self, request):
        # 1，接收前端数据
        # 接收前端body
        body_bytes = request.body
        # 转码成字符串
        body_str = body_bytes.decode()
        # 转json
        body_dict = json.loads(body_str)
        # 2，获取数据
        username = body_dict.get('username')
        password = body_dict.get('password')
        password2 = body_dict.get('password2')
        mobile = body_dict.get('mobile')
        allow = body_dict.get('allow')
        # 3，数据校验
        # all([xxx,xxx,xxx,...]):all里的元素只要是None/False，表达式就会返回False，否则返回True
        if not all([username, password, password2, mobile, allow]):
            return JsonResponse({'code': 400, 'errMsg': '请检查输入内容'})
        if not re.match('[a-zA-Z0-9_-]{5,20}', username):
            return JsonResponse({'code': 400, 'errMsg': '用户名不符合要求'})
        if len(password) < 8 or len(password) > 20:
            return JsonResponse({'code': 400, 'errMsg': '密码不符合要求'})
        if password2 != password:
            return JsonResponse({'code': 400, 'errMsg': '两次密码输入不一致'})
        if not re.match('1[3-9]\\d{9}', mobile):
            return JsonResponse({'code': 400, 'errMsg': '手机号码不符合要求'})
        if not allow:
            return JsonResponse({'code': 400, 'errMsg': '同意后才可注册'})
        # 4，数据入库
        # 方式1
        # user = User(username=username, password=password, mobile=mobile)
        # user.save()
        # 方式2
        # User.objects.create(username=username, password=password, mobile=mobile)
        # 方式3（落库时密码是加密保存的）
        user = User.objects.create_user(username=username, password=password, mobile=mobile)
        # session登录状态保持，session保存在redis中
        login(request, user)
        return JsonResponse({'code': 0, 'errMsg': 'OK'})


class LoginView(View):
    '''
    登录请求
    '''

    def post(self, request):
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        remembered = data.get('remembered')
        if not all([username, password]):
            return JsonResponse({'code': 400, 'errMsg': '请输入用户名/密码'})
        # 支持用户名/手机号登录，此处判断具体使用何种属性去进行登录验证
        if re.match('1[3-9]\\d{9}', username):
            User.USERNAME_FIELD = 'mobile'
        else:
            User.USERNAME_FIELD = 'username'
        # 验证用户密码是否正确：使用django提供的方法实现，底层逻辑就是使用用户密码查询数据库
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'code': 400, 'errMsg': '账号/密码不正确'})
        # 验证通过，记录session
        login(request, user)
        # 判断是否“记住我”
        if remembered is not None:
            # 记住登录，默认记住两周
            request.session.set_expiry(None)
        else:
            # 不记住登录，浏览器关闭后，清空session
            request.session.set_expiry(0)
        response = JsonResponse({'code': 0, 'errMsg': 'OK'})
        # 让前端可以从cookie从获取'username'的value进行展示
        response.set_cookie('username', username)
        return response


class LogoutView(View):
    '''
    退出登录请求
    '''

    def delete(self, request):
        # 利用django自带函数实现退出登录功能，本质上就是删除session
        logout(request)
        response = JsonResponse({'code': 0, 'errMsg': 'OK'})
        # 删除指定的cookie
        response.delete_cookie('username')
        return response


class LoginRequiredJsonMixin(AccessMixin):
    """方式一：模仿 LoginRequiredMixin 类改写 return JsonResponse({'code': 0, 'errMsg': 'no login'}) """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'code': 0, 'errMsg': 'no login'})
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixinOverride(LoginRequiredMixin):
    """方式二：继承 LoginRequiredMixin 类，重写 handle_no_permission 函数 """

    def handle_no_permission(self):
        return JsonResponse({'code': 0, 'errMsg': 'no login'})


class CenterView(LoginRequiredMixinOverride, View):
    '''
    跳转“用户中心”
    1，要解决未登录用户重定向django自带页面问题，改为返回json数据（提供以上的方式一/二，两种解决方案）
    '''

    def get(self, request):
        # request.user 是已经登录用户的信息
        info_data = {
            'username': request.user.username,
            'email': request.user.email,
            'mobile': request.user.mobile,
            'email_active': request.user.email_active,
        }
        return JsonResponse({'code': 0, 'errMsg': 'OK', 'info_data': info_data})


class EmailView(LoginRequiredMixinOverride, View):
    '''
    处理“添加邮箱”业务
    本功能是基于“登录用户”开发的，所以也要继承LoginRequiredMixinOverride，来获取登录用户的信息
    '''

    def put(self, request):
        data = json.loads(request.body.decode())
        email = data.get('email')
        # 获取登录用户 User对象，并赋值给实例 user
        user = request.user
        user.email = email
        user.save()
        # 邮件主题
        subject = '来自python客户端的一封信'
        # 邮件内容
        message = '这里是要说的话'
        # 发件人
        from_email = 'wu43456229@163.com'
        # 收件人列表
        # to_list = ['wu43456229@163.com', '543456229@qq.com']
        to_list = ['wu43456229@163.com']
        # 使用user_id获取加密后的token
        token = generic_email_verify_token(request.user.id)
        verify_url = settings.VERIFY_URL + '?token=%s' % token
        # html标签的msg
        html_message = "点击按钮进行激活 <a href='%s'>激活</a>" % verify_url
        # html_message = "点击按钮进行激活 <a href='http://www.baidu.com/?token=%s'>激活</a>"%token

        # 异步发送邮件
        celery_send_email.delay(subject=subject, message=message, from_email=from_email,
                                to_list=to_list, html_message=html_message)

        # 同步发送
        # send_mail(subject=subject, message=message, from_email=from_email,
        #           recipient_list=to_list, html_message=html_message)

        return JsonResponse({'code': 0, 'errMsg': 'OK'})


class EmailVerifyView(View):
    '''
    处理“邮箱激活”业务
    '''

    def put(self, request):
        params = request.GET
        token = params.get('token')
        if token is None:
            return JsonResponse({'code': 400, 'errMsg': '未获取到token'})
        user_id = check_verify_token(token)
        if user_id is None:
            return JsonResponse({'code': 400, 'errMsg': '未获取到user_id'})
        # 通过user_id获取user对象
        user = User.objects.get(id=user_id)
        user.email_active = True
        user.save()
        return JsonResponse({'code': 0, 'errMsg': 'OK'})


class AddressCreateView(LoginRequiredMixinOverride, View):
    '''
    处理“新增收货地址”业务
    '''

    def post(self, request):
        # 判断是否超过地址数量上限
        count = request.user.addresses.count()
        if count >= 20:
            return JsonResponse({'code': 400, 'errMsg': '超过地址数量上限'})
        # 将前端请求数据转为json
        data = json.loads(request.body.decode())
        receiver = data.get('receiver')
        province_id = data.get('province_id')
        city_id = data.get('city_id')
        district_id = data.get('district_id')
        place = data.get('place')
        mobile = data.get('mobile')
        tel = data.get('tel')
        email = data.get('email')
        user = request.user
        # 参数校验（非法校验略）
        if not all([receiver, province_id, city_id, district_id, place, mobile]):
            return JsonResponse({'code': 400, 'errMsg': '请检查输入内容'})
        # 数据落库
        new_address = Address.objects.create(
            user=user,
            title=receiver,
            receiver=receiver,
            province_id=province_id,
            city_id=city_id,
            district_id=district_id,
            place=place,
            mobile=mobile,
            tel=tel,
            email=email
        )
        address = {
            'id': new_address.id,
            "title": new_address.title,
            "receiver": new_address.receiver,
            "province": new_address.province.name,
            "city": new_address.city.name,
            "district": new_address.district.name,
            "place": new_address.place,
            "mobile": new_address.mobile,
            "tel": new_address.tel,
            "email": new_address.email
        }
        return JsonResponse({'code': 0, 'errMsg': 'OK', 'address': address})


class AddressView(LoginRequiredMixinOverride, View):
    '''
    查询 收货地址
    '''

    def get(self, request):
        user = request.user
        addresses = Address.objects.filter(user=user, is_deleted=False)
        address_list = []
        for address in addresses:
            address_list.append({
                "id": address.id,
                "title": address.title,
                "receiver": address.receiver,
                "province": address.province.name,
                "city": address.city.name,
                "district": address.district.name,
                "place": address.place,
                "mobile": address.mobile,
                "tel": address.tel,
                "email": address.email
            })
        return JsonResponse({'code': 0, 'errMsg': 'OK', 'addresses': address_list})
