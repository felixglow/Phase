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

        response = HttpResponse(content_type='application/json')  # 优先从cookie中取
        txt_d, txt_n, sug, tmp_max, tmp_min, code, txt, now_tmp = request.COOKIES.get('txt_d'), request.COOKIES.get('txt_n'), \
                                                                  request.COOKIES.get('sug'), request.COOKIES.get('tmp_max'), \
                                                                  request.COOKIES.get('tmp_min'), request.COOKIES.get('code'), \
                                                                  request.COOKIES.get('now_tmp'), request.COOKIES.get('txt')

        if (not (txt_d and txt_n and sug and tmp_max and tmp_min and code and txt and now_tmp)) \
                or (not request.session.get('user_ip') == ip):
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
                tmp_max = result['daily_forecast'][0]['tmp']['max']
                tmp_min = result['daily_forecast'][0]['tmp']['min']
                code = result['now']['cond']['code']
                txt = result['now']['cond']['txt']
                now_tmp = result['now']['tmp']

                # 存储天气相关cookie
                expires_time = datetime.datetime.now() + datetime.timedelta(hours=3)
                tmp_list = [['txt_d', txt_d], ['txt_n', txt_n], ['sug', sug], ['tmp_max', tmp_max],
                            ['tmp_min', tmp_min], ['code', code], ['now_tmp', now_tmp], ['txt', txt]]
                map(lambda x: response.set_cookie(x[0], x[1], expires=expires_time), tmp_list)

        res = {
            'msg': hy + u'\n\n你想做什么?\n天呐!你是不是暗恋我! ^_^' + u"\n\n好了,友情提示: 今天" + area + u" (白天" + txt_d +
                   u' 夜间' + txt_n + u' 温度最高' + tmp_max + u'°C 最低' + tmp_min + '°C)\n' + sug,
        }
        response.write(json.dumps(res))
        return response