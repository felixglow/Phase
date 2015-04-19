# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import View, ListView, TemplateView

from .models import Article, About, Tag


class Index(ListView):
    """
    博客首页
    """

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_active=True, is_published=True).order_by('-publish_time')
        new_articles = articles[:6]
        recommend_articles = articles.filter(is_recommend=True)[:8]
        return render_to_response('index.html', {'articles': new_articles, 'recommends': recommend_articles})


class AboutMe(TemplateView):
    """
    关于我
    """

    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        about = About.objects.filter(is_active=True)

        return self.render_to_response({"about": about[0] if about else []})


class Share(TemplateView):
    """
    分享
    """

    template_name = 'share.html'

    def get(self, request, *args, **kwargs):

        return self.render_to_response({})


class BlogList(ListView):
    """
    爱折腾列表
    """

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_active=True, is_published=True, is_life=False).order_by('-publish_time')
        tags = Tag.objects.filter(count__gt=0, is_active=True)
        tops = articles.order_by('-click_count')[:8]
        recommends = articles.filter(is_recommend=True)[:8]
        return render_to_response('blog.html', {'articles': articles, 'tags': tags, 'tops': tops, 'recommends': recommends})


class BlogDetail(TemplateView):
    """
    爱折腾详情
    """

    template_name = 'blog_detail.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=request.GET.get('id', 1))
        article.click()
        tags = Tag.objects.filter(count__gt=0, is_active=True)
        return self.render_to_response({'article': article, 'tags': tags})


class TagQuery(ListView):
    """
    根据标签查询
    """

    def get(self, request):
        tag = get_object_or_404(Tag, pk=request.GET.get('id', None))
        articles = tag.article_set.filter(is_active=True, is_published=True).order_by('-publish_time')
        tags = Tag.objects.filter(count__gt=0, is_active=True)
        arts = Article.objects.filter(is_active=True, is_published=True).order_by('-publish_time')
        tops = arts.order_by('-click_count')
        recommends = arts.filter(is_recommend=True)

        return render_to_response('blog.html', {'articles': articles, 'tags': tags, 'tops': tops, 'recommends': recommends})


class LifeList(ListView):
    """
    乐生活列表
    """

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_active=True, is_published=True, is_life=True).order_by('-publish_time')
        tops = articles.order_by('-click_count')[:8]
        recommends = articles.filter(is_recommend=True)[:8]
        return render_to_response('life.html', {'articles': articles, 'tops': tops, 'recommends': recommends})


class LifeDetail(TemplateView):
    """
    乐生活详情
    """

    template_name = 'life_detail.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=request.GET.get('id', 1))
        article.click()
        return self.render_to_response({'article': article})





