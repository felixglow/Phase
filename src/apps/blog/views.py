# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.http import Http404

from base.views import BaseView
from base.mixins import JsonResponseMixin, LoginRequireMixin, PaginateMixin
from .models import Article, Tag
from base.utils import check_visit


class BlogList(BaseView, PaginateMixin):
    """
    爱折腾列表
    """

    page_size = 6
    TOP_ARTICLE_NUM = 5
    RECOMMEND_ARTICLE_NUM = 5
    template_name = 'blog/blog.html'

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


class BlogDetail(BaseView):
    """
    爱折腾详情
    """

    template_name = 'blog/blog_detail.html'
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
        next_art = articles.filter(publish_time__gt=article.publish_time).order_by('publish_time')[:1]
        before_art = articles.filter(publish_time__lt=article.publish_time).order_by('-publish_time')[:1]

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

    page_size = 6
    TOP_ARTICLE_NUM = 5
    RECOMMEND_ARTICLE_NUM = 5
    template_name = 'blog/blog.html'

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



