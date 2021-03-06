# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VOD',
            fields=[
                ('vod_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('all_messages_loaded', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='vod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vod_stats.VOD'),
        ),
    ]
