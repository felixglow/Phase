# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from views import Index, Blog


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view(), name="Index"),
    url(r'^blog/$', Blog.as_view(), name="blog")
)
