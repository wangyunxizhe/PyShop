from django.utils.deprecation import MiddlewareMixin

"""
自定义django中间件，用于处理 请求前 以及 响应前 的业务，类似于java中filter的作用。
需要在/pyShop/settings.py--MIDDLEWARE注册才能生效
"""


class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print("每次 请求前 都会调用执行~~~~No.1111~~~~")
        username = request.COOKIES.get("name")
        if username is None:
            print("没有用户信息")
        else:
            print("有用户信息")

    def process_response(self, request, response):
        print("每次 响应前 都会调用执行~~~~No.1111~~~~")
        return response


"""
当同时注册两个自定义中间件时，注意每次 请求前 以及 响应前 的”执行顺序“：
request是按照No.1111--》No.2222，而response是按照No.2222--》No.1111
"""


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print("每次 请求前 都会调用执行~~~~No.2222~~~~")

    def process_response(self, request, response):
        print("每次 响应前 都会调用执行~~~~No.2222~~~~")
        return response
