import os
from threading import Thread
from time import sleep

from vod_stats.twitch_api import TwitchAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TwitchWutFace.settings")

import django

django.setup()
from vod_stats.models import *


class ChatMessageLoader(Thread):
    def __init__(self, vod, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(ChatMessageLoader, self).__init__(group, target, name, args, kwargs, verbose)
        self.vod = vod

    def run(self):
        timestamp_offset = 0
        while timestamp_offset < vod.duration:
            messages = TwitchAPI().get_chat_messages(vod.vod_id, vod.timestamp + timestamp_offset)
            print messages
            for message in messages:
                ChatMessage(vod=vod).save()
            timestamp_offset += 30

while (True):
    print "Searching for incomplete jobs..."
    vods = VOD.objects.filter(all_messages_loaded=False, load_in_progress=False)
    for vod in vods:
        print "Starting loading for {0}".format(vod.vod_id)
        vod.load_in_progress = True
        vod.save()
        ChatMessageLoader(vod).start()

    sleep(5)
