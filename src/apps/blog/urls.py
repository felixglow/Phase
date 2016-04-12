# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.conf.urls import patterns, url
from .views import BlogDetail, BlogList, TagQuery


urlpatterns = patterns('',
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^list/(?P<page>\d+)/$', BlogList.as_view(), name="blog_list_page"),
    url(r'^(?P<id>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^tag/query/(?P<id>\d+)/$', TagQuery.as_view(), name="tag_query"),
)