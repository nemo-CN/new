# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class IndexBanerInfo(models.Model):
    img = models.ImageField()
    a = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    p = models.CharField(max_length=100)
    status = models.SmallIntegerField(null=True)

class IndexMovieInfo(models.Model):
    img = models.ImageField()
    a = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class IndexBullhornInfo(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    publisher = models.CharField(max_length=30)
    times = models.CharField(max_length=20)
    a_link = models.CharField(max_length=100)
    sort_id = models.SmallIntegerField(null=True)
    hot_id = models.SmallIntegerField(null=True)

class IndexCaseInfo(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    a_link = models.CharField(max_length=100)


class UserManage(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30,default="123456")
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    status = models.SmallIntegerField(null=True)
    DoManage = models.ForeignKey('DoManage', null=True, blank=True, on_delete=models.SET_NULL)

class DoManage(models.Model):
    username = models.CharField(max_length=30)
    createtime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    Permissions = models.CharField(max_length=50, null=True)

class MenuTree(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=50)

class Permissions(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    MenuTree = models.ForeignKey('MenuTree', null=True, blank=True, on_delete=models.SET_NULL)

class UserRole(models.Model):
    UserManage = models.ForeignKey("UserManage", null=True, blank=True, on_delete=models.SET_NULL)
    DoManage = models.ForeignKey("DoManage", null=True, blank=True, on_delete=models.SET_NULL)

class MessageNum(models.Model):
    MessageNum = models.IntegerField()
    createtime = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank = True, null = True)
    author = models.CharField(max_length=30)
    uptime = models.CharField(max_length=30)
    createtime = models.DateTimeField(auto_now_add=True)