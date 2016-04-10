# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from apps.blog.views import BlogList


class Index(BlogList):
    """
    博客首页
    """

    template_name = 'index/index.html'