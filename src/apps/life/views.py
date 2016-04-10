# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.http import Http404

from base.views import BaseView
from base.mixins import JsonResponseMixin, LoginRequireMixin, PaginateMixin
from apps.blog.models import Article
from base.utils import check_visit


class LifeList(BaseView, PaginateMixin):
    """
    慢生活列表
    """

    page_size = 6
    TOP_ARTICLE_NUM = 5
    template_name = 'life/life.html'

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

    template_name = 'life/life_detail.html'
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

        next_art = articles.filter(publish_time__gt=article.publish_time).order_by('publish_time')[:1]
        before_art = articles.filter(publish_time__lt=article.publish_time).order_by('-publish_time')[:1]

        kwargs.update({
            'article': article,
            'tops': tops,
            'next_art': next_art[0] if next_art else '',
            'before_art': before_art[0] if before_art else ''
        })
        return super(LifeDetail, self).get(request, **kwargs)