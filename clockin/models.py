
from django.db import models

# Create your models here.

class Cust(models.Model):
    """ 用户 """
    id = models.AutoField(primary_key=True, verbose_name='id')
    no = models.CharField(max_length=32, blank=True, verbose_name='用户的no')
    newat = models.DateField(auto_now_add=False, verbose_name='新建日期')

    class Meta:
        db_table = 'cust'
        verbose_name = '用户表'


class ClockType(models.Model):
    """ 用户的打卡类型 """
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=20, blank=True, verbose_name='打卡类型')
    newat = models.DateField(auto_now_add=False, verbose_name='新建日期')
    upat = models.DateField(auto_now=False, verbose_name='更新日期')
    cust = models.ForeignKey(to=Cust, db_column="custId", on_delete=models.PROTECT, verbose_name="所属用户")

    class Meta:
        db_table ='clocktype'
        verbose_name ='用户的打卡类型'

from enum import Enum

class DefaultType(models.Model):
    """ 默认打卡类型 """

    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=40, blank=True, unique=True, verbose_name='默认类型名称')

    class Meta:
        db_table = 'defaulttype'
        verbose_name ='默认打卡类型'


class Clcok(models.Model):
    """ 打卡 """
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=20, blank=True, verbose_name='打卡名称')
    newat = models.DateField(auto_now_add=False, verbose_name='新建日期')
    upat = models.DateField(auto_now=False, verbose_name='更新日期')
    cust = models.ForeignKey(to=Cust, db_column="custId", on_delete=models.PROTECT, verbose_name="所属用户")
    clockType = models.ForeignKey(to=ClockType, db_column="clockTypeId", on_delete=models.PROTECT, verbose_name="所属打卡类型")

    class Meta:
        db_table ='clock'
        verbose_name ='打卡表'


class Record(models.Model):
    """ 打卡记录 """
    id = models.AutoField(primary_key=True, verbose_name='id')
    newat = models.DateField(auto_now_add=False, verbose_name='打卡日期')
    cust = models.ForeignKey(to=Cust, db_column="custId", on_delete=models.PROTECT, verbose_name="所属用户")
    clock = models.ForeignKey(to=Clcok, db_column="clockId", on_delete=models.PROTECT, verbose_name="所属打卡")

    class Meta:
        db_table ='record'
        verbose_name ='打卡记录表'