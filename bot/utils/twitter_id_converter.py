from tweepy import API, Cursor
from tweepy.error import TweepError
import re


class Converter:
    def __init__(self, config, auth):
        self.config = config
        self.client = API(auth)

    def convert(self) -> dict:
        for instance in self.config["Discord"]:
            tmp_twitter_ids = []
            if "twitter_lists" in instance.keys() and not instance["twitter_lists"] in [
                None,
                "",
                [],
                [""],
            ]:
                for twitter_list in instance["twitter_lists"]:
                    tmp_twitter_ids += self.twitter_list_to_id(twitter_list)
            if "twitter_handles" in instance.keys() and not instance["twitter_handles"] in [
                None,
                "",
                [],
                [""],
            ]:
                tmp_twitter_ids += self.twitter_handle_to_id(instance["twitter_handles"])
            if "twitter_ids" not in instance:
                instance["twitter_ids"] = list()
            instance["twitter_ids"].extend(
                x for x in tmp_twitter_ids if x not in instance["twitter_ids"]
            )
            if "" in instance["twitter_ids"]:
                instance["twitter_ids"].remove("")
            if tmp_twitter_ids:
                print(
                    "{amount} twitter ids have been added through twitter list.".format(
                        amount=len(tmp_twitter_ids)
                    )
                )

        # throw out config that don't have a webhook url
        self.config["Discord"] = [
            {k: v for k, v in instance.items() if instance.get("webhook_urls", [])}
            for instance in self.config["Discord"]
        ]

        # throw out config that have empty twitter_ids, track and location
        self.config["Discord"] = [
            {
                k: v
                for k, v in instance.items()
                if instance.get("twitter_ids", [])
                or instance.get("track", [])
                or instance.get("location", [])
            }
            for instance in self.config["Discord"]
        ]

        # throw out empty config
        while {} in self.config["Discord"]:
            self.config["Discord"].remove({})

        return self.config

    def twitter_list_to_id(self, twitter_list_url: str) -> list:
        twitter_ids = []
        pattern = "(https?:\/\/(?:www\.)?)?twitter\.com\/(?P<twittername>[a-zA-Z0-9]+)\/lists\/(?P<listname>[a-zA-Z0-9-]+)"
        for m in re.finditer(pattern, twitter_list_url, re.I):
            try:
                for member in Cursor(
                    self.client.list_members, m.group("twittername"), m.group("listname")
                ).items():
                    twitter_id = member._json["id_str"]
                    if twitter_id not in twitter_ids:
                        twitter_ids.append(twitter_id)
            except TweepError as e:
                print(e)
        return twitter_ids

    def twitter_handle_to_id(self, twitter_handles: list) -> list:
        full_users = []
        user_count = len(twitter_handles)
        for i in range(0, int((user_count // 100)) + 1):
            try:
                full_users.extend(
                    self.client.lookup_users(
                        screen_names=twitter_handles[i * 100 : min((i + 1) * 100, user_count)]
                    )
                )
            except TweepError as e:
                print(e)
        return [user.id_str for user in full_users]


if __name__ == "__main__":
    import sys

    sys.path.append("..")
    from config import config, auth

    c = Converter(config, auth)
    print(c.convert())
