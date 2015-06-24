# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.conf.urls import patterns, include, url
from django.conf import settings
from views import Index, AboutMe, ShareList, BlogDetail, BlogList, TagQuery, LifeList, LifeDetail


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name="index"),
    url(r'^blog/list/$', BlogList.as_view(), name="blog_list"),
    url(r'^blog/list/(?P<page>\d+)/$', BlogList.as_view(), name="blog_list_page"),
    url(r'^blog/detail/(?P<id>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^life/list/$', LifeList.as_view(), name="life_list"),
    url(r'^life/list/(?P<page>\d+)/$$', LifeList.as_view(), name="life_page_list"),
    url(r'^life/detail/(?P<id>\d+)/$', LifeDetail.as_view(), name="life_detail"),
    url(r'^share/$', ShareList.as_view(), name="share"),
    url(r'^share/(?P<page>)\d+/$', ShareList.as_view(), name="share_page"),
    url(r'^tag/query/(?P<id>\d+)/$', TagQuery.as_view(), name="tag_query"),
    url(r'^about/$', AboutMe.as_view(), name="about"),
)
