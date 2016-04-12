# -*-coding:utf-8 -*-
# 
# Created on 2016-04-12, by felix
#

__author__ = 'felix'

import requests
import IP
import json
import datetime

from django.conf import settings
from django.http import HttpResponse

from base.mixins import JsonResponseMixin
from base.views import BaseView


class Weather(BaseView, JsonResponseMixin):
    """
    天气
    """

    def get(self, request, *args, **kwargs):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        request.session['user_ip'] = ip
        area = ''.join(set(IP.find(ip).split('\t')))
        hy = u'欢迎来自' + area + u'的朋友~~~'

        response = HttpResponse(content_type='application/json')
        txt_d, txt_n, sug = request.COOKIES.get('txt_d'), request.COOKIES.get('txt_n'), request.COOKIES.get('sug')
        if (not txt_d and not txt_n and not sug) or (not request.session.get('user_ip') == ip):
            try:
                url = 'https://api.heweather.com/x3/weather?cityip=%s&key=%s' % (ip, settings.WEATHER_KEY)
                r = requests.get(url)
                result = r.json().values()[0][0]
            except IndexError:
                return self.render_json_to_response(result={'msg': hy})
            else:
                if not result.get('status') == 'ok':
                    return self.render_json_to_response(result={'msg': hy})
                txt_d = result['daily_forecast'][0]['cond']['txt_d']
                txt_n = result['daily_forecast'][0]['cond']['txt_n']
                sug = result['suggestion']['comf']['txt'] if result.has_key('suggestion') else ''
                expires_time = datetime.datetime.now() + datetime.timedelta(hours=3)
                response.set_cookie('txt_d', txt_d, expires=expires_time)
                response.set_cookie('txt_n', txt_n, expires=expires_time)
                response.set_cookie('sug', sug, expires=expires_time)
        res = {
            'msg': hy + u'\n\n你想做什么?\n天呐!你是不是暗恋我! ^_^' + u"\n\n好了,友情提示: 今天" + area + u" 白天" + txt_d + u' 夜间' + txt_n + '\n' + sug,
        }
        response.write(json.dumps(res))
        return response