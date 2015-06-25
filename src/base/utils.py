# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-25, by felix
# 
# 

__author__ = 'felix'

import datetime

from django.utils import timezone


def check_visit(request):
    now = timezone.now().date().strftime('%Y-%m-%d')
    ip = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']

    if ip in request.session:
        last_time = request.session[ip]
        if last_time == now:
            return False
        else:
            request.session[ip] = now
            return True
    else:
        request.session[ip] = now
        return True
