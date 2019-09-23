from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,  HttpResponse
import json
from .models import *
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def addCust(request):
    """ 新增用户 """
    # 分配默认的打卡类型
    Cust.objects.create(no=request.GET('custNo'))

    for name, _ in DefaultType.__members__.items():
        ClockType.objects.create(name=name)


def addClockType(request):
    """ 新增打卡类型 """
    pass

def addClock(request):
    """ 新增打卡 """
    pass

def addRecord(request):
    """ 新增打卡记录 """
    pass

def getDefType(request):
    "获取默认的打卡类型"
    typeList = DefaultType.objects.all()
    
    json_data = serializers.serialize('json', typeList)
    json_data = json.loads(json_data)

    print(json_data)

    return JsonResponse(json_data, json_dumps_params={'ensure_ascii':False}, safe=False)
    