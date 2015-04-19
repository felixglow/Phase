# -*-coding:utf-8 -*-
#
# Created on 2015-01-22, by chengbin.wang
#
#

__author__ = 'chengbin.wang'


from django.db import models
from core.models import BaseModel
from DjangoUeditor.models import UEditorField
from django.db.models.signals import post_delete, m2m_changed


class Tag(BaseModel):
    name = models.CharField(verbose_name=u'名称', max_length=20)
    count = models.IntegerField(verbose_name=u'数量', default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    def decr(self, num=1):
        self.count -= num
        self.save()

    def incr(self, num=1):
        self.count += num
        self.save()


class Article(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'标题')
    tags = models.ManyToManyField(Tag, verbose_name=u'标签', blank=True, null=True)
    author = models.CharField(max_length=15, verbose_name=u'作者')
    image = models.ImageField(verbose_name=u'文章图片', upload_to='article')
    content = UEditorField(verbose_name=u'正文', width=1200, height=900, imagePath='blogs/')
    is_recommend = models.BooleanField(verbose_name=u'是否推荐', default=False)
    is_published = models.BooleanField(verbose_name=u'是否发布', default=False)
    is_life = models.BooleanField(verbose_name=u'是否生活', default=False)
    click_count = models.IntegerField(default=0, editable=False, verbose_name=u'点击量')
    comment_count = models.IntegerField(default=0, editable=False, verbose_name=u'评论数')
    publish_time = models.DateTimeField(verbose_name=u'发布时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def click(self):
        self.click_count += 1
        self.save()


def handle_in_batches(instances, method):
    for item in instances:
        getattr(item, method)()


def article_post_delete(sender, **kwargs):
    ins = kwargs.get('instance')
    handle_in_batches(ins.tags.all(), 'decr')


def change_tags(sender, **kwargs):
    if kwargs.get('action') == 'pre_clear':
        handle_in_batches(kwargs.get('instance').tags.all(), 'decr')
    elif kwargs.get('action') == 'post_remove':
        handle_in_batches(Tag.objects.filter(id__in=kwargs.get('pk_set')), 'decr')
    elif kwargs.get('action') == 'post_add':
        handle_in_batches(Tag.objects.filter(id__in=kwargs.get('pk_set')), 'incr')


post_delete.connect(article_post_delete, sender=Article)
m2m_changed.connect(change_tags, sender=Article.tags.through)


class About(BaseModel):
    """
    关于我
    """

    name = models.CharField(max_length=50, verbose_name=u'标题')
    content = UEditorField(verbose_name=u'正文', width=1200, height=900, imagePath='about/')
    click_count = models.IntegerField(default=0, verbose_name=u'点击量')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'关于我'
        verbose_name_plural = u'关于我'






