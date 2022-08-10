
from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def Index(request):
    count = 0

    Test.objects.create(name= "Name" )
    count = count + 1
    return HttpResponse(count)

def Shows(request):
    datas = Test.objects.all()
    return HttpResponse(datas)