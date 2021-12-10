from random import randint

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha
from utils.sendMessage import RongLianUtils


class ImageCodeView(View):
    '''
    图片验证码
    '''

    def get(self, request, uuid):
        # 利用 libs/captcha 中的第三方SDK，生成图片验证码（text）和图片二进制（image）
        text, image = captcha.generate_captcha()
        # 连接redis，使用setting.py中的code配置redis库
        redis_cli = get_redis_connection('code')
        # 将验证码信息存入redis，100为过期时间，单位秒
        redis_cli.setex(uuid, 100, text)
        # 将图片二进制返回前端，并告知前端response的类型，用于生成图片
        return HttpResponse(image, content_type='image/jpeg')


class SmsCodeView(View):
    '''
    短信验证码
    '''

    def get(self, request, mobile):
        # 获取请求参数
        image_code = request.GET.get("image_code")
        uuid = request.GET.get("image_code_id")
        # 参数验证
        if not all([image_code, uuid]):
            return JsonResponse({'code': 400, 'errmsg': '参数不全'})
        # 校验图片验证码：通过了图片验证码校验再发短信，防止浪费短信发送费用
        redis_cli = get_redis_connection('code')
        redis_image_code = redis_cli.get(uuid)
        if redis_image_code is None:
            return JsonResponse({'code': 400, 'errmsg': '图片验证码已过期'})
        if redis_image_code.decode().lower() != image_code.lower():
            return JsonResponse({'code': 400, 'errmsg': '图片验证码输入错误'})
        # 校验是否是频繁操作
        send_flag = redis_cli.get('send_flag_%s' % mobile)
        if send_flag is not None:
            return JsonResponse({'code': 400, 'errmsg': '请勿频繁发送短信'})
        # 生成短信验证码
        sms_code = '%06d' % randint(0, 999999)

        # 在这里使用pipeline方式和redis交互以达到多条命令一次执行，减少IO成本，提升性能的效果
        pipeline = redis_cli.pipeline()
        # 将短信验证码存入redis
        pipeline.setex(mobile, 300, sms_code)
        # 为避免频繁操作导致的频繁发送短信，需要加入此类操作验证
        pipeline.setex('send_flag_%s' % mobile, 60, 'haved')
        pipeline.execute()

        # 不使用pipeline
        # 将短信验证码存入redis
        # redis_cli.setex(mobile, 300, sms_code)
        # 为避免频繁操作导致的频繁发送短信，需要加入此类操作验证
        # redis_cli.setex('send_flag_%s' % mobile, 60, 'haved')

        # 使用容联云发送短信
        RongLianUtils().send_message(text=sms_code, minute=3)
        return JsonResponse({'code': 0, 'errmsg': 'ok'})
