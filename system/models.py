#coding:utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    id  = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length= 100,null=False)
    password = models.CharField(max_length=100,null=False)
    creat_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'User'
        app_label = 'system'

    def __str__(self):
        return str(self.id)



