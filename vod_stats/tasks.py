from celery import shared_task
from celery_once import QueueOnce

from twitch_api import TwitchAPI
from models import VOD, ChatMessage


@shared_task(base=QueueOnce)
def download_chat_messages(vod_id, timestamp, duration):
    api = TwitchAPI()
    vod = VOD.objects.get(id=vod_id)
    timestamp_offset = 0

    while timestamp_offset < duration:
        timestamp_offset += 30
        try:
            data = api.get_chat_messages(vod_id, timestamp + timestamp_offset)
            if data["data"]:
                for message in data["data"]:
                    db_message = ChatMessage(id=message["id"],
                                             message=message["attributes"]["message"],
                                             timestamp=message["attributes"]["timestamp"],
                                             vod=vod)
                    db_message.save()

        except:
            continue

    vod.all_messages_loaded = True
    vod.save()
