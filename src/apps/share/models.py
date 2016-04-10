# -*-coding:utf-8 -*-
# 
# Created on 2016-04-07, by felix
# 

__author__ = 'felix'

from django.db import models
from core.models import BaseModel
from DjangoUeditor.models import UEditorField


class Share(BaseModel):
    """
    乐分享
    """

    name = models.CharField(max_length=50, verbose_name=u'标题')
    image = models.ImageField(verbose_name=u'文章图片', upload_to='share')
    content = UEditorField(verbose_name=u'正文', width=1200, height=900, imagePath='share/')
    publish_time = models.DateTimeField(verbose_name=u'发布时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'乐分享'
        verbose_name_plural = u'乐分享'
