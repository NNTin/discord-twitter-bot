from tweepy import API, Cursor
import re


class Converter:
    def __init__(self, config, auth):
        self.config = config
        self.client = API(auth)

    def convert(self) -> dict:
        tmp_twitter_ids = []
        for instance in self.config["Discord"]:
            if "twitter_lists" in instance.keys() and not instance["twitter_lists"] in [None, ""]:
                for twitter_list in instance["twitter_lists"]:
                    tmp_twitter_ids += self.twitter_list_to_id(twitter_list)
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
        return self.config

    def twitter_list_to_id(self, twitter_list_url: str) -> list:
        twitter_ids = []
        pattern = "(https?:\/\/(?:www\.)?)?twitter\.com\/(?P<twittername>[a-zA-Z0-9]+)\/lists\/(?P<listname>[a-zA-Z0-9-]+)"
        for m in re.finditer(pattern, twitter_list_url, re.I):
            for member in Cursor(
                self.client.list_members, m.group("twittername"), m.group("listname")
            ).items():
                twitter_id = member._json["id_str"]
                if twitter_id not in twitter_ids:
                    twitter_ids.append(twitter_id)
        return twitter_ids

    def twitter_handle_to_id(self) -> list:
        raise NotImplemented()


if __name__ == "__main__":
    test = "hallo, jhfds"
    print(test.split(","))
    import sys

    sys.path.append("..")
    from config import config, auth

    c = Converter(config, auth)
    print(config)
    # print(c.twitter_list_to_id("https://twitter.com/rokxx/lists/dota-2"))
    print(c.convert())
    print(config)
