# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.contrib import admin
from .models import Article, Tag
from django.utils.html import format_html


# class AdminMixin(object):
#
#     def show_image(self, obj):
#         html = "<img src={0} width=120 height=80>"
#         return format_html(html.format(obj.image.url))
#     show_image.short_description = u'图片'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')
    readonly_fields = ('count',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish_time')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
