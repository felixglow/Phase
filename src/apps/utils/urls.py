# -*-coding:utf-8 -*-
# 
# Created on 2016-04-12, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import Weather


urlpatterns = patterns('',
    url(r'^weather/$', Weather.as_view(), name="weather_get"),
)