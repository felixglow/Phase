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

from apps.index.views import Index

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^management/backend/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^life/', include('apps.life.urls')),
    # url(r'^magic/', include('apps.magic.urls')),
    url(r'^share/', include('apps.share.urls')),
    url(r'^utils/', include('apps.utils.urls')),
)


urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                        )