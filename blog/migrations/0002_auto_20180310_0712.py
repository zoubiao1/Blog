# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-10 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogarticle',
            old_name='type',
            new_name='article_type',
        ),
    ]
