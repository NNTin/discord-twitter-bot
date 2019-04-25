#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import Stream
from time import gmtime, strftime
from time import sleep
import urllib3
import requests

try:
    from utils.processor import Processor
except ModuleNotFoundError:
    from bot.utils.processor import Processor
try:
    from config import config, auth
except ModuleNotFoundError:
    from bot.config import config, auth
try:
    from utils.twitter_id_converter import Converter
except ModuleNotFoundError:
    from bot.utils.twitter_id_converter import Converter
try:
    from utils.startup import pprint
except ModuleNotFoundError:
    from bot.utils.startup import pprint


class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super().__init__(api)
        self.config_discord = config["Discord"]

    def _on_status(self, status):
        data = status._json

        for data_discord in self.config_discord:
            p = Processor(status_tweet=data, discord_config=data_discord)
            p.get_text()

            if (
                not p.worth_posting_follow()
                and not p.worth_posting_track()
                and not p.worth_posting_location()
            ):
                continue

            if not p.keyword_set_present():
                continue

            if p.blackword_set_present():
                continue

            for wh_url in data_discord.get("webhook_urls", []):
                p.create_embed()
                p.attach_media()

                p.send_message(wh_url)

                print(
                    strftime("[%Y-%m-%d %H:%M:%S]", gmtime()),
                    data["user"]["screen_name"],
                    "twittered.",
                )

    def on_status(self, status):
        """Called when a new status arrives"""
        try:
            self._on_status(status)
        except Exception as error:
            print(
                f"---------Error---------\n"
                f"unknown error\n"
                f"You've found an error. Please contact the owner (https://discord.gg/JV5eUB) "
                f"and send him what follows below:\n"
                f"{error}\n"
                f"{status}"
                f"-----------------------"
            )


if __name__ == "__main__":
    print("Bot started.")
    config = Converter(config, auth).convert()
    print(config)
    follow = []
    track = []
    location = []
    for element in config["Discord"]:
        follow.extend(x for x in element.get("twitter_ids", []) if x not in follow)
        track.extend(x for x in element.get("track", []) if x not in track)
        location.extend(x for x in element.get("location", []))

    pprint(config)

    l = StdOutListener()
    stream = Stream(auth, l)

    print("Twitter stream started.")
    while True:

        def print_error(_error):
            print(
                f"---------Error---------\n"
                f"Known error. Ignore. Nothing you can do.\n"
                f"{_error}\n"
                f"Sleeping for 1 minute then continuing.\n"
                f"-----------------------"
            )
            sleep(600)

        try:
            stream.filter(follow=follow, track=track, locations=location)
        except urllib3.exceptions.ProtocolError as error:
            print_error(_error=error)
        except ConnectionResetError as error:
            print_error(_error=error)
        except ConnectionError as error:
            print_error(_error=error)
        except requests.exceptions.ConnectionError as error:
            print_error(_error=error)
        except Exception as error:
            print(
                f"---------Error---------\n"
                f"unknown error\n"
                f"You've found an error. Please contact the owner (https://discord.gg/JV5eUB) "
                f"and send him what follows below:\n"
                f"{error}\n"
                f"{config}\n"
                f"Sleeping for 5 minute then continuing.\n"
                f"Twitter streaming continues.\n"
                f"-----------------------"
            )
            sleep(3000)
