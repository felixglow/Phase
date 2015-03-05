# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#
__author__ = 'chengbin.wang'


from django.db import models
from core.models import BaseModel
from DjangoUeditor.models import UEditorField


class Article(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'标题')
    image = models.ImageField(verbose_name=u'文章图片', upload_to='article')
    content = UEditorField(verbose_name=u'文章内容', width=1200, height=900, imagePath='article/content')
    publish_time = models.DateTimeField(verbose_name=u'发布时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

