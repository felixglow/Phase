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


class Blog(View):

    def get(self, request):
        return render_to_response('blog.html')
