# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-10 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180310_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogarticle',
            old_name='content_id',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='gmt_create',
            field=models.DateTimeField(help_text='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
