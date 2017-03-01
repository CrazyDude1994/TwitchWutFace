from __future__ import unicode_literals

from django.db import models


class VOD(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    duration = models.IntegerField()
    timestamp = models.IntegerField()
    all_messages_loaded = models.BooleanField(default=False, blank=True)


class ChatMessage(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    message = models.TextField()
    timestamp = models.IntegerField()
    vod = models.ForeignKey(VOD, on_delete=models.CASCADE)
