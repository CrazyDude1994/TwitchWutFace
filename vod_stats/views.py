from celery_once import AlreadyQueued
from django.core.exceptions import ObjectDoesNotExist

from django.http.response import HttpResponse
from django.shortcuts import render

from django.core import serializers

from models import VOD
from tasks import download_chat_messages

# Create your views here.
from vod_stats.models import ChatMessage
from vod_stats.twitch_api import TwitchAPI
from vod_stats.utils import get_timestamp_from_str


def main_view(request):
    return render(request, 'index.html')


def chat_data(request, video_id):
    try:
        db_vod = VOD.objects.get(id=video_id)
        if not db_vod.all_messages_loaded:
            try:
                download_chat_messages.delay(video_id, db_vod.timestamp, db_vod.duration)
            except AlreadyQueued:
                pass
    except ObjectDoesNotExist:
        vod = TwitchAPI().get_vod_info(video_id)
        db_vod = VOD(id=video_id, duration=vod["length"], timestamp=get_timestamp_from_str(vod["recorded_at"]))
        db_vod.save()
        download_chat_messages.delay(video_id, db_vod.timestamp, db_vod.duration)

    messages = ChatMessage.objects.filter(vod=db_vod)
    return HttpResponse(serializers.serialize("json", messages), content_type="application/json")
