# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import ShareList


urlpatterns = patterns('',
    url(r'^$', ShareList.as_view(), name="share"),
    url(r'^(?P<page>\d+)/$', ShareList.as_view(), name="share_page"),
)