from tweepy import OAuthHandler, Stream
from main import StdOutListener
import os
from dataIO import fileIO

if __name__ == '__main__':
    if not fileIO("data.json", "check"):
        print("data.json does not exist. Creating empty data.json...")
        fileIO("data.json", "save", {
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
                        "webhook_urls": os.environ["WEBHOOK_URL"].replace(" ", "").split(","),
                        "twitter_ids": os.environ["TWITTER_ID"].replace(" ", "").split(",")
                    }
                ]
            }
        )

    data_t = fileIO("data.json", "load")

    print('Bot started.')

    data_t['twitter_ids'] = []
    for element in data_t['Discord']:
        data_t['twitter_ids'].extend(x for x in element['twitter_ids'] if x not in data_t['twitter_ids'])

    print('{} Twitter users are being followed.'.format(len(data_t['twitter_ids'])))

    l = StdOutListener(datad=data_t["Discord"])
    auth = OAuthHandler(data_t['Twitter']['consumer_key'], data_t['Twitter']['consumer_secret'])
    auth.set_access_token(data_t['Twitter']['access_token'], data_t['Twitter']['access_token_secret'])
    stream = Stream(auth, l)

    print('Twitter stream started.')
    stream.filter(follow=data_t['twitter_ids'])