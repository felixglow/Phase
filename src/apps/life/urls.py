# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import LifeList, LifeDetail


urlpatterns = patterns('',
    url(r'^$', LifeList.as_view(), name="life_list"),
    url(r'^list/(?P<page>\d+)/$$', LifeList.as_view(), name="life_page_list"),
    url(r'^(?P<id>\d+)/$', LifeDetail.as_view(), name="life_detail"),
)