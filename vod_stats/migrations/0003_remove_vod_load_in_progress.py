# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vod_stats', '0002_auto_20170227_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vod',
            name='load_in_progress',
        ),
    ]