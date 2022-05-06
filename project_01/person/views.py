from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def peopleinfo(request):
    return HttpResponse("路由到这里")