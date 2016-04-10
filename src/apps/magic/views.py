# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from base.views import BaseView


class MagicList(BaseView):
    """
    炫魔方
    """

    template_name = 'magic/magic.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


class SiWa(BaseView):
    """
    撕袜
    """

    template_name = 'magic/siwa.html'