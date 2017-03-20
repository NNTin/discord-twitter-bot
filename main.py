#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from discordWebhooks import Webhook, Attachment, Field
import calendar
import time
import json
import secret

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            data = json.loads(data)
            print(data['created_at'])

            wh = Webhook(url=secret.WEBHOOK_URL, username="Chirp",
                         icon_url="http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_lg.png")
            at = Attachment(author_name=data['user']['screen_name'],
                            author_icon=data['user']['profile_image_url'].replace('\\', ''),
                            color="#ffffff", pretext=data['text'].replace('\\', ''),
                            title_link="https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']),
                            footer="Tweet created at",
                            footer_icon="https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png",
                            ts=calendar.timegm(time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')))

            wh.addAttachment(at)
            wh.post()
        except:
            print(data)
            print(type(data))
            raise Exception("TODO: Analyze error (if it exists).")

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
    auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['soccer', 'basketball'])
    #stream.filter(follow=['<twitter id>', '<twitter id>'])
