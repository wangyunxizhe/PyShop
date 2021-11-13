from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha


class ImageCodeView(View):

    def get(self, request, uuid):
        # 利用 libs/captcha 中的第三方SDK，生成图片验证码（text）和图片二进制（image）
        text, image = captcha.generate_captcha()
        # 连接redis，使用setting中的code配置redis库
        redis_cli = get_redis_connection('code')
        # 将验证码信息存入redis，100为过期时间，单位秒
        redis_cli.setex(uuid, 100, text)
        # 将图片二进制返回前端，并告知前端response的类型，用于生成图片
        return HttpResponse(image, content_type='image/jpeg')
