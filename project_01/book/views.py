from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
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
    print(Query_params)
    order = Query_params.getlist('keys')
    print(order)
    return HttpResponse("分店")

def school(request,prince_id,city_id,school_id):
    print(prince_id,city_id,school_id)

    return HttpResponse("高校系统")

"""
查询字符串
IP：PORT/path/path/?key1=value1 & key2=value2.....



"""

