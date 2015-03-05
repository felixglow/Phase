# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.shortcuts import render, render_to_response
from django.views.generic import View, ListView

from .models import Article


class Index(ListView):
    queryset = Article.objects.filter().order_by('-publish_time')[:3]
    context_object_name = 'article_obj'
    template_name = 'index.html'


class Blog(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'article_obj'
    template_name = 'blog.html'
