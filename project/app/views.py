from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse("welcome all")
def fun2(req,a):
    return HttpResponse(a)