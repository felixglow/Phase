# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'

from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        abstract = True
