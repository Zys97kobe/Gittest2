"""
中间件
设置中间件类，继承自MiddlewareMixin，重写父类的方法

然后在setting中的MIDDLEWARE中注册中间件。

"""
from django.utils.deprecation import MiddlewareMixin
class TestMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print("每次请求前 都会调用 中间件1111")
    def process_response(self,request,response):
        print("每次响应前，都会调用 中间件1111")
        return response

class TestMiddleWare2(MiddlewareMixin):

    def process_request(self,request):
        print("每次请求前 都会调用 中间件2222")
    def process_response(self,request,response):
        print("每次响应前，都会调用 中间件2222")
        return response