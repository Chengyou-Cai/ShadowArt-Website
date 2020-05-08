# -*- coding: utf-8 -*-
from __future__ import  unicode_literals #声明文件用utf8编码
from django.db import models #Django模型类必须继承自django.db.models


#新增用于设置消息类型枚举项
KIND_CHOICES=(
    ('python','python'),
    ('database','database'),
    ('economic','economic'),
)

# Create your models here.

# 定义models的子类Moment，其中定义3个字符串类型的字段
class Moment(models.Model):
    id=models.AutoField(primary_key=True)
    headline=models.CharField(max_length=255,default="test")
    body_text=models.TextField(default="default")
    pub_date=models.DateField(auto_now=True)
    n_visits=models.IntegerField(default=0)

    content = models.CharField(max_length=200) #保存信息内容
    user_name = models.CharField(max_length=20,default='匿名') #保存发布人姓名
    kind = models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0]) #保存消息类型,修改后加入choices参数

    def __str__(self):
        return "id{} headline{}".format(self.id,self.headline)

class Mytable(models.Model):
    id = models.CharField(max_length=20, blank=True, primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)        

    class Meta:
        managed = True
        db_table = 'mytable'