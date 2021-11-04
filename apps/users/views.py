import json
import re

from django.contrib.auth import login
from django.http import JsonResponse
from django.views import View
from apps.users.models import User


class UsernameCountView(View):

    def get(self, request, username):
        # 以下操作使用 utils/converters.py 中的自定义转换器来完成
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 200, 'errMsg': '用户名不符合要求'})
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 200, 'count': count, 'errMsg': 'OK'})


class RegisterView(View):

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
