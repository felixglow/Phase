# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.shortcuts import render, render_to_response
# Create your views here.
from django.views.generic import View


class Index(View):

    def get(self, request):
        return render_to_response('index.html')
