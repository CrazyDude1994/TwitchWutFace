import urllib2
import json


class TwitchAPI:
    API_URL = "https://api.twitch.tv/kraken/"

    def __init__(self, client_id="q8x5vxmvt3si7q0s0ibx1dayxfojdjw"):
        self.client_id = client_id

    def get_vod_info(self, vod_id):
        data = urllib2.urlopen(self._construct_twitch_api_request("videos/{0}".format(vod_id)))
        return json.loads(data.read())

    def _construct_twitch_api_request(self, url):
        return urllib2.Request(TwitchAPI.API_URL + url, headers={"Client-ID": self.client_id})

    def get_chat_messages(self, vod_id, timestamp):
        data = urllib2.urlopen(
            "https://rechat.twitch.tv/rechat-messages?start={0}&video_id={1}".format(timestamp, vod_id))
        return json.loads(data.read())
