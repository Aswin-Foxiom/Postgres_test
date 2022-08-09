
from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def Index(request):
    Test.objects.create(name="Second")
    return HttpResponse("OK")

def Shows(request):
    datas = Test.objects.all()
    return HttpResponse(datas)