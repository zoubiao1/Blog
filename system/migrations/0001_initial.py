# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-10 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('creat_time', models.DateTimeField()),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
