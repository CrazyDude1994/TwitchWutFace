from django.core.exceptions import ObjectDoesNotExist

from django.http.response import HttpResponse
from django.shortcuts import render

from models import VOD

# Create your views here.
from vod_stats.twitch_api import TwitchAPI
from vod_stats.utils import get_timestamp_from_str


def main_view(request):
    return render(request, 'index.html')


def chat_data(request, video_id):
    try:
        db_vod = VOD.objects.get(vod_id=video_id)
    except ObjectDoesNotExist:
        vod = TwitchAPI().get_vod_info(video_id)
        db_vod = VOD(vod_id=video_id, duration=vod["length"], timestamp=get_timestamp_from_str(vod["recorded_at"]))
        db_vod.save()
    return HttpResponse(db_vod.timestamp)

    # return HttpResponse(data.read(), content_type="application/json")
