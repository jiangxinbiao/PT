from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
import uuid
import os
class Label(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=30)
    updatetime = models.DateField(verbose_name='修改时间', auto_now=True)
    createtime = models.DateField(verbose_name='创建时间', auto_now_add=True)
    class Meta:
        verbose_name = u'作品标签'
        verbose_name_plural = verbose_name
        db_table = 'Label'
        ordering = ['-updatetime']
    def __str__(self):
        return self.name


class Painting(models.Model):
    name = models.CharField(verbose_name='作品名称',max_length=50,null=True,blank=True)
    photo = models.ImageField(verbose_name='作品',upload_to='avatar', height_field='url_height', width_field='url_width')
    url_height = models.PositiveIntegerField(verbose_name='图片宽',null=True,blank=True)
    url_width = models.PositiveIntegerField(verbose_name='图片长',null=True,blank=True)
    Ph = models.IntegerField(verbose_name='作品长',null=True,blank=True,)
    Pt = models.IntegerField(verbose_name='作品宽',null=True,blank=True)
    Cname = models.CharField(verbose_name='作者名',max_length=50,null=True,blank=True)
    Createtime = models.DateField(verbose_name='创作时间',auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    text = UEditorField(verbose_name=u'作品说明', width=850, height=500, toolbars="full", imagePath="media/images/", filePath="media/files/",
	                       upload_settings={"imageMaxSize": 1204000},
	                       settings={}, command=None, blank=True,null = True)
    label = models.ManyToManyField(Label,verbose_name='标签')   #作品标签关联作品 多对多关系
    class Meta:
        verbose_name = u'作品'
        verbose_name_plural = verbose_name
        db_table = 'painting'
        ordering = ['-updated']
    def __str__(self):
        return self.name

class Comments(models.Model):
    post = models.ForeignKey(Painting,verbose_name='作品',on_delete=models.CASCADE,null = True)
    name = models.CharField(verbose_name='昵称', max_length=16, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱')
    body = models.TextField(verbose_name='评论正文',null=True,blank=True)
    created = models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null = True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
        db_table = 'comment'
        ordering = ['created']
    def __str__(self):
        return 'Comments by {} on {}'.format(self.name, self.post)

class AdminIMG(models.Model):
    filename = models.CharField(verbose_name='文件名',max_length=200,blank=True,null=True)
    img = models.ImageField(upload_to='./admin')
