# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-28 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0002_auto_20180927_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_by',
        ),
    ]
