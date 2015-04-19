# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from views import Index, AboutMe, Share, BlogDetail, BlogList, TagQuery, LifeList, LifeDetail


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name="index"),
    url(r'^about/$', AboutMe.as_view(), name="about"),
    url(r'^share/$', Share.as_view(), name="share"),
    url(r'^blog/list/$', BlogList.as_view(), name="blog_list"),
    url(r'^blog/detail/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^life/list/$', LifeList.as_view(), name="life_list"),
    url(r'^life/detail/$', LifeDetail.as_view(), name="life_detail"),
    url(r'^tag/query/$', TagQuery.as_view(), name="tag_query"),
)
