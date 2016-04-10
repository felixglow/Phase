# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import MagicList, SiWa


urlpatterns = patterns('',
    url(r'^list/$', MagicList.as_view(), name="magic"),
    url(r'^siwa/$', SiWa.as_view(), name="siwa"),
)