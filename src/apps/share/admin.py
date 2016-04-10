# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.contrib import admin
from .models import Share


class ShareAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Share, ShareAdmin)