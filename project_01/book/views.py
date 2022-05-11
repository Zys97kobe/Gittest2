from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book,Userinfo

# Create your views here.
def create_book(request):
    # book = Book.objects.create(
    #     name='python',
    #     pub_date='2020-2-2',
    #     author='IDK',
    #     readcount=25,
    # )
    return HttpResponse("create")
def delete_book(requset):
    Book.objects.filter(name='python').delete()
    return  HttpResponse("delete")

def shop(request,city_id,shop_id):

    Query_params = request.GET
    # 查询字符串，字典类型，{key:value},
    # 但是Query_params可以一Key多value
    order = Query_params.getlist('keys')
    print(order)
    return HttpResponse("分店")

def school(request,prince_id,city_id,school_id):
    # 验证占位符是否符合条件。


    print(prince_id,city_id,school_id)

    return HttpResponse("高校系统")

"""FORM 表单 JSON 数据的接受"""
def register(request):
    # FORM表单用request.POST获取数据
    qs = request.POST

    if len(qs)==0:
    # JSON数据则需要用request.body获得
        qs = request.body# 此时的qs为bytes类型的数据

    qs_str = qs.decode() # decode将bytes转化为str类型
    """ 
    此时是JSON样式的 str数据，我们要把它转化为 python的字典使用 json.loads()
        {
            "username":"caiwenjuan",
            "password":"123456"        
        }
    """
    import json
    qs = json.loads(qs_str)

    # 获取POST的FORM表单，然后用字典操作，进行数据库输入

    Userinfo.objects.create(username = qs.get("username"),
                            password = qs.get("password"),)
    return HttpResponse("注册操作")

"""查看请求类型"""
def method(request):

    return HttpResponse("请求类型为：%s" % request.method)

"""Httpresponse"""
# HttpResponse(content = 响应体,content_type = 响应体类型,status = 状态码)

def response(request):
    http = HttpResponse("response",status=200)
    http["name"]='zhangyongsheng'
    return http


"""JsonResponse"""
from django.http import JsonResponse
def jsresponse(request):
    friends = [
        {
            "name":"caiwenjuan",
            "add":"shanghai"
        }
        ,
        {
            "name": "daiweijian",
            "add": "shandong"
        }
        ,
        {
            "name":"chengxuhan",
            "add":"shandong"
        }
    ]
    # safe = True 表示 data为字典数据，JsonResponese可以将字典转换为json
    # data不是字典时，需要将safe设为False
    return JsonResponse(data = friends,safe=False)

"""重定向"""
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
def Redirect(request):

    return HttpResponseRedirect('https://www.baidu.com/')

"""设置Cookie"""
"""
第一次请求携带查询字符串
服务器接收到请求之后，获取username,服务器设置cookie信息，cookie信息包括username
浏览器接受服务器响应之后，保存cookie

第二次之后的请求，访问127.0.0.1都会携带cookie信息。
http://127.0.0.1/set_Cookie/?username=zhangyongsheng&password=123456
"""

def set_Cookie(request):
    # 获取查询字符串的信息
    qs = request.GET
    cookie_name = list(qs.keys())[0]
    # 服务器设置cookie信息
    # 响应对象.set_cookie()
    response = HttpResponse('Set Cookie')
    response.set_cookie(cookie_name,qs.get(cookie_name),max_age=60)
    return response
def get_Cookie(request):
    # 服务器获取cookie信息，获取的为字典类型。
    cookieInfo = request.COOKIES.get("name")
    return HttpResponse("Get Cookieinfo:%s" %cookieInfo)
def del_Cookie(request):
    response = HttpResponse("Del Cookie")
    response.delete_cookie('name')
    #相当于set_cookie中将max_age设为0
    return response