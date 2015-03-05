# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.contrib import admin
from .models import Article
from django.utils.html import format_html


class AdminMixin(object):

    def show_image(self, obj):
        html = "<img src={0} width=120 height=80>"
        return format_html(html.format(obj.image.url))
    show_image.short_description = u'图片'


class ArticleAdmin(admin.ModelAdmin, AdminMixin):
    list_display = ('name', 'show_image', 'publish_time')


admin.site.register(Article, ArticleAdmin)
