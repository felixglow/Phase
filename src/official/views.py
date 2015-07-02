# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#

__author__ = 'chengbin.wang'


from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404

from base.mixins import JsonResponseMixin, LoginRequireMixin, PaginateMixin
from base.views import BaseView, ListView
from .models import Article, About, Tag, Share
from base.utils import check_visit


class BlogList(BaseView, PaginateMixin):
    """
    爱折腾列表
    """

    page_size = 5
    TOP_ARTICLE_NUM = 5
    RECOMMEND_ARTICLE_NUM = 5
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_active=True, is_published=True, is_life=False).order_by('-publish_time')
        tags = Tag.objects.filter(count__gte=0, is_active=True)
        tops = articles.order_by('-click_count')[:self.TOP_ARTICLE_NUM]
        recommends = articles.filter(is_recommend=True)[:self.RECOMMEND_ARTICLE_NUM]

        page_obj, queryset = self.paginate_queryset(articles, self.page_size)
        kwargs.update({
            'articles': queryset,
            'tags': tags,
            'tops': tops,
            'recommends': recommends,
            'page_obj': page_obj
        })
        return super(BlogList, self).get(request, **kwargs)


class Index(BlogList):
    """
    博客首页
    """

    template_name = 'index.html'


class BlogDetail(BaseView):
    """
    爱折腾详情
    """

    template_name = 'blog_detail.html'
    TOP_ARTICLE_NUM = 5
    RECOMMEND_ARTICLE_NUM = 5

    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')
        try:
            article = Article.objects.get(id=blog_id, is_active=True)
        except (Article.DoesNotExist, ValueError):
            raise Http404()

        if check_visit(request, blog_id):
            article.click()  # 增加点击次数

        articles = Article.objects.filter(is_active=True, is_published=True, is_life=False).order_by('-publish_time')
        tops = articles.order_by('-click_count')[:self.TOP_ARTICLE_NUM]
        recommends = articles.filter(is_recommend=True)[:self.RECOMMEND_ARTICLE_NUM]
        tags = Tag.objects.filter(count__gte=0, is_active=True)

        next_art = articles.filter(id__gt=article.id).order_by('id')[:1]
        before_art = articles.filter(id__lt=article.id).order_by('-id')[:1]

        kwargs.update({
            'article': article,
            'tags': tags,
            'tops': tops,
            'recommends': recommends,
            'next_art': next_art[0] if next_art else '',
            'before_art': before_art[0] if before_art else ''
        })
        return super(BlogDetail, self).get(request, **kwargs)


class TagQuery(BaseView, PaginateMixin):
    """
    根据标签查询
    """

    page_size = 5
    TOP_ARTICLE_NUM = 5
    RECOMMEND_ARTICLE_NUM = 5
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=kwargs.get('id'), is_active=True)
        except (Tag.DoesNotExist, ValueError):
            raise Http404

        articles = tag.article_set.filter(is_active=True, is_published=True).order_by('-publish_time')
        tags = Tag.objects.filter(count__gte=0, is_active=True)
        arts = Article.objects.filter(is_active=True, is_published=True).order_by('-publish_time')
        tops = arts.order_by('-click_count')[:self.TOP_ARTICLE_NUM]
        recommends = arts.filter(is_recommend=True)[:self.RECOMMEND_ARTICLE_NUM]

        page_obj, queryset = self.paginate_queryset(articles, self.page_size)
        kwargs.update({
            'articles': queryset,
            'tags': tags,
            'tops': tops,
            'recommends': recommends,
            'page_obj': page_obj
        })

        return super(TagQuery, self).get(request, **kwargs)


class LifeList(BaseView, PaginateMixin):
    """
    慢生活列表
    """

    page_size = 5
    TOP_ARTICLE_NUM = 5
    template_name = 'life.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_active=True, is_published=True, is_life=True).order_by('-publish_time')
        tops = articles.order_by('-click_count')[:self.TOP_ARTICLE_NUM]

        page_obj, queryset = self.paginate_queryset(articles, self.page_size)
        kwargs.update({'articles': queryset, 'tops': tops, 'page_obj': page_obj})

        return super(LifeList, self).get(request, **kwargs)


class LifeDetail(BaseView):
    """
    慢生活详情
    """

    template_name = 'life_detail.html'
    TOP_ARTICLE_NUM = 5

    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')
        try:
            article = Article.objects.get(id=blog_id, is_active=True)
        except (Article.DoesNotExist, ValueError):
            raise Http404()

        if check_visit(request, blog_id):
            article.click()  # 增加点击次数

        articles = Article.objects.filter(is_active=True, is_published=True, is_life=True).order_by('-publish_time')
        tops = articles.order_by('-click_count')[:self.TOP_ARTICLE_NUM]

        next_art = articles.filter(id__gt=article.id).order_by('id')[:1]
        before_art = articles.filter(id__lt=article.id).order_by('-id')[:1]

        kwargs.update({
            'article': article,
            'tops': tops,
            'next_art': next_art[0] if next_art else '',
            'before_art': before_art[0] if before_art else ''
        })
        return super(LifeDetail, self).get(request, **kwargs)


class ShareList(BaseView, PaginateMixin):
    """
    分享
    """

    page_size = 5
    template_name = 'share.html'

    def get(self, request, *args, **kwargs):
        share = Share.objects.filter(is_active=True).order_by('-publish_time')

        page_obj, queryset = self.paginate_queryset(share, self.page_size)
        kwargs.update(share=queryset, page_obj=page_obj)

        return super(ShareList, self).get(request, **kwargs)


class AboutMe(BaseView):
    """
    关于我
    """

    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        about = About.objects.filter(is_active=True)

        kwargs.update({"about": about[0] if about else ''})
        return super(AboutMe, self).get(request, **kwargs)
