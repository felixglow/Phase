# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from base.mixins import JsonResponseMixin, LoginRequireMixin, PaginateMixin
from base.views import BaseView
from .models import Share


class ShareList(BaseView, PaginateMixin):
    """
    分享
    """

    page_size = 6
    template_name = 'share/share.html'

    def get(self, request, *args, **kwargs):
        share = Share.objects.filter(is_active=True).order_by('-publish_time')

        page_obj, queryset = self.paginate_queryset(share, self.page_size)
        kwargs.update(share=queryset, page_obj=page_obj)

        return super(ShareList, self).get(request, **kwargs)