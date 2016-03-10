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
    now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    if str(id) not in request.session:
        request.session[str(id)] = now
        return True
    else:
        if (timezone.now().replace(tzinfo=None) - datetime.datetime.strptime(request.session[str(id)], '%Y-%m-%d %H:%M:%S')).seconds >= 6*60*60:
            request.session[str(id)] = now
            request.session.modified = True
            return True
        return False
