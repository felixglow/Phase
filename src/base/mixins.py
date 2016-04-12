# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by felix
# 
#

__author__ = 'felix'

import json

from django.http import HttpResponse, Http404
from django.utils.translation import ugettext as _
from django.core.paginator import InvalidPage, Paginator
from core.codes import CODES


class JsonResponseMixin(object):
    """
    返回json数据
    """

    content_type = 'application/json'

    def render_json_to_response(self, status='0', *args, **kwargs):
        res = {
            'status': status,
            'message': CODES[status]['msg'],
            'result': kwargs.get('result')
        }
        return HttpResponse(json.dumps(res), content_type=self.content_type)


class LoginRequireMixin(object):
    """
    登录限制
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponseMixin.render_json_to_response(status='2')
        return super(LoginRequireMixin, self).dispatch(request, *args, **kwargs)


class PaginateMixin(object):
    """
    分页
    """

    allow_empty = True
    paginate_orphans = 0
    paginator_class = Paginator
    page_kwarg = 'page'

    def range_list(self, page):
        num = page.number
        total = page.paginator.num_pages
        if num <= 5:
            return page.paginator.page_range[:6]
        elif num > total - 3:
            return page.paginator.page_range[total-6:total]
        else:
            return page.paginator.page_range[num-3:num+3]

    def paginate_queryset(self, queryset, page_size):
        """
        Paginate the queryset, if needed.
        """
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
            page.range_list = self.range_list(page)
            return page, page.object_list
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True, **kwargs):
        """
        Return an instance of the paginator for this view.
        """
        return self.paginator_class(
            queryset, per_page, orphans=orphans,
            allow_empty_first_page=allow_empty_first_page, **kwargs)

    def get_paginate_orphans(self):
        """
        Returns the maximum number of orphans extend the last page by when
        paginating.
        """
        return self.paginate_orphans

    def get_allow_empty(self):
        """
        Returns ``True`` if the view should display empty lists, and ``False``
        if a 404 should be raised instead.
        """
        return self.allow_empty




