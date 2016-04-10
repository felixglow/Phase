# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import Index


urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name="index"),
                       )