from utils.dataIO import fileIO
import os

false_strings = ["false", "False", "f", "F", "0", "", "n", "N", "no", "No", "NO", "FALSE"]

if fileIO("config.json", "check"):
    config = fileIO("config.json", "load")
else:
    config = {
        "Twitter": {
            "consumer_key": os.environ["CONSUMER_KEY"],
            "consumer_secret": os.environ["CONSUMER_SECRET"],
            "access_token": os.environ["ACCESS_TOKEN"],
            "access_token_secret": os.environ["ACCESS_TOKEN_SECRET"]
        },
        "Discord": [
            {
                "IncludeReplyToUser": False if os.environ["INCLUDE_REPLY_TO_USER"] in false_strings else True,
                "IncludeRetweet": False if os.environ["INCLUDE_RETWEET"] in false_strings else True,
                "IncludeUserReply": False if os.environ["INCLUDE_USER_REPLY"] in false_strings else True,
                "webhook_urls": os.environ["WEBHOOK_URL"].replace(" ", "").split(","),
                "twitter_ids": os.environ["TWITTER_ID"].replace(" ", "").split(","),
                "custom_message": os.environ.get("CUSTOM_MESSAGE", None)
            }
        ],
        "twitter_ids": []
    }
    keyword_sets = os.environ.get("KEYWORDS", None)
    if keyword_sets:
        keyword_sets = [keyword_set.split("+") for keyword_set in keyword_sets.replace(" ", "").split(",")]
        config["Discord"][0]["keyword_sets"] = keyword_sets
