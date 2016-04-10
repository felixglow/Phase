# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
#

__author__ = 'felix'

import qrcode
import StringIO

from django.shortcuts import render
from django.http import HttpResponse

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


class Qrcode(BaseView):
    """
    二维码生成
    """

    template_name = 'magic/qrcode.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('create'):
            error_correct = {
                'L': qrcode.constants.ERROR_CORRECT_L,
                'M': qrcode.constants.ERROR_CORRECT_M,
                'Q': qrcode.constants.ERROR_CORRECT_Q,
                'H': qrcode.constants.ERROR_CORRECT_H
            }
            qr = qrcode.QRCode(version=5, box_size=request.GET.get('size'), border=2,
                               error_correction=error_correct.get(request.GET.get('error_correct')))
            qr.add_data(request.GET.get('data'))
            qr.make(fit=True)
            img = qr.make_image()
            img_buffer = StringIO.StringIO()
            img.save(img_buffer)
            return HttpResponse(img_buffer.getvalue(), 'image/jpeg')
        return self.render_to_response({})
