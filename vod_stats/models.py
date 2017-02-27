from __future__ import unicode_literals

from django.db import models

# Create your models here.


class VOD(models.Model):
    vod_id = models.CharField(max_length=20, primary_key=True)
    duration = models.IntegerField()
    timestamp = models.IntegerField()
    all_messages_loaded = models.BooleanField(default=False, blank=True)
    load_in_progress = models.BooleanField(default=False)


class ChatMessage(models.Model):
    message = models.TextField()
    timestamp = models.IntegerField()
    vod = models.ForeignKey(VOD, on_delete=models.CASCADE)
