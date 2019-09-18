from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def addCust(request):
    """ 新增用户 """
    # 分配默认的打卡类型
    pass

def addClockType(request):
    """ 新增打卡类型 """
    pass

def addClock(request):
    """ 新增打卡 """
    pass

def addRecord(request):
    """ 新增打卡记录 """
    pass
