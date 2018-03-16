#coding:utf8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogArticleContent(models.Model):
    '''
    文章内容表
    '''
    id = models.AutoField(primary_key=True)
    content_text = models.TextField(help_text='文本内容')
    gmt_create = models.DateTimeField(auto_now_add=True,help_text='创建时间')
    gmt_modified = models.DateTimeField(help_text='修改时间')

    class Meta:
        db_table = 'blog_article_content'
        app_label = 'blog'

    def __str__(self):
        return str(self.id)



class BlogArticle(models.Model):
    '''
    文章表
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000,null=True,help_text='标题')
    TYPE_CHOICES = (
        ('0','原创'),
        ('1','转发'),
        ('2','翻译')
                 )
    article_type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    content = models.ForeignKey(BlogArticleContent,db_constraint = False,null=True,on_delete=models.SET_NULL,help_text='关联内容表id')
    STATUS_CHOICES = (
        ('draft','草稿'),
        ('on_line','在线'),
        ('out_line','下线'),
    )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,help_text='状态')
    classify = models.CharField(max_length=100,help_text='分类')
    custom_classify = models.CharField(max_length=100,help_text='自定义分类')
    gmt_create = models.DateTimeField(help_text='创建时间')
    gmt_modified = models.DateTimeField(help_text='修改时间')

    class Meta:
        db_table = 'blog_article'
        app_label = 'blog'

    def __str__(self):
        return str(self.id)
