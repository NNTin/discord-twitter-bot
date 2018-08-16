from dataIO import fileIO
import os

false_strings = ["false", "False", "f", "F", "0", ""]

if fileIO("data.json", "check"):
    data_json = fileIO("data.json", "load")
else:
    data_json = {
        "Twitter": {
            "consumer_key": os.environ["CONSUMER_KEY"],
            "consumer_secret": os.environ["CONSUMER_SECRET"],
            "access_token": os.environ["ACCESS_TOKEN"],
            "access_token_secret": os.environ["ACCESS_TOKEN_SECRET"]
        },
        "Discord": [
            {
                "IncludeReplyToUser": True,
                "IncludeRetweet": True,
                "IncludeUserReply": True,
                "webhook_urls": os.environ.get("WEBHOOK_URL", []).replace(" ", "").split(","),
                "twitter_ids": os.environ.get("TWITTER_ID", []).replace(" ", "").split(",")
            }
        ],
        "twitter_ids": []
    }
