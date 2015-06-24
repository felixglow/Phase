# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include("official.urls")),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                        )