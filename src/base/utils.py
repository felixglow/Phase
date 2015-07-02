# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-25, by felix
# 
# 

__author__ = 'felix'

import datetime

from django.utils import timezone


def check_visit(request, id):
    now = timezone.now().strftime('%Y-%m-%d')
    # ip = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']

    if str(id) not in request.session:
        request.session[str(id)] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        return True
    else:
        if (timezone.now().replace(tzinfo=None) - datetime.datetime.strptime(request.session[str(id)], '%Y-%m-%d %H:%M:%S')).seconds >= 12*60*60:
            request.session[str(id)] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            request.session.modified = True
            return True
        return False
