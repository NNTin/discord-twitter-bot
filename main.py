from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from tweepy.api import API
from discordWebhooks import Webhook, Embed, Field
import calendar, datetime, time, random, json
from time import gmtime, strftime
from datetime import datetime
import html

class StdOutListener(StreamListener):
    def __init__(self, api=None):
        self.api = api or API()


    def on_status(self, status):
        """Called when a new status arrives"""

        colors = [0x7f0000, 0x535900, 0x40d9ff, 0x8c7399, 0xd97b6c, 0xf2ff40, 0x8fb6bf, 0x502d59, 0x66504d,
                  0x89b359, 0x00aaff, 0xd600e6, 0x401100, 0x44ff00, 0x1a2b33, 0xff00aa, 0xff8c40, 0x17330d,
                  0x0066bf, 0x33001b, 0xb39886, 0xbfffd0, 0x163a59, 0x8c235b, 0x8c5e00, 0x00733d, 0x000c59,
                  0xffbfd9, 0x4c3300, 0x36d98d, 0x3d3df2, 0x590018, 0xf2c200, 0x264d40, 0xc8bfff, 0xf23d6d,
                  0xd9c36c, 0x2db3aa, 0xb380ff, 0xff0022, 0x333226, 0x005c73, 0x7c29a6]

        data = status._json
        #print(data)

        with open('data.json') as data_file:
            dataD = json.load(data_file)

        for dataDiscord in dataD['Discord']:


            if 'IncludeReplyToUser' in dataDiscord:     #other Twitter user tweeting to your followed Twitter user
                if dataDiscord['IncludeReplyToUser'] == False:
                    if data['user']['id_str'] not in dataDiscord['twitter_ids']:
                        #print('Random Twitter user tweeted to your followed twitter users')
                        continue
            else:   #if not specified: default behavior is not to include
                if data['user']['id_str'] not in dataDiscord['twitter_ids']:
                    continue

            if 'IncludeUserReply' in dataDiscord:       #your followed Twitter users tweeting to random Twitter users (relevant if you only want status updates/opt out of conversations)
                if dataDiscord['IncludeUserReply'] == False:
                    if data['user']['id_str'] in dataDiscord['twitter_ids']:
                        if data['in_reply_to_user_id'] is not None:
                            if data['in_reply_to_user_id'] not in dataDiscord['twitter_ids']:
                                if 'retweeted_status' not in data:
                                    #print('Your followed twitter users tweeted to someone else')
                                    continue

            if 'IncludeRetweet' in dataDiscord:         #retweets...
                if dataDiscord['IncludeRetweet'] == False:
                    if 'retweeted_status' in data:
                        #print('This is a retweeted status')
                        continue



            for wh_url in dataDiscord['webhook_urls']:

                username = data['user']['screen_name']
                icon_url = data['user']['profile_image_url']


                text = ''
                if 'extended_tweet' in data:
                    text = data['extended_tweet']['full_text']
                else:
                    text = data['text']

                for url in data['entities']['urls']:
                    if url['expanded_url'] == None:
                        continue
                    text = text.replace(url['url'], "[%s](%s)" %(url['display_url'],url['expanded_url']))

                for userMention in data['entities']['user_mentions']:
                    text = text.replace('@%s' %userMention['screen_name'], '[@%s](https://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))

                media_url = ''
                media_type = ''
                if 'extended_tweet' in data:
                    if 'media' in data['extended_tweet']['entities']:
                        for media in data['extended_tweet']['entities']['media']:
                            if media['type'] == 'photo':
                                media_url = media['media_url']

                if 'media' in data['entities']:
                    for media in data['entities']['media']:
                        if media['type'] == 'photo' and not media_url:
                            media_url = media['media_url_https']
                            media_type = 'photo'
                        if media['type'] == 'video':
                            media_url = media['media_url_https']
                            media_type = 'photo'
                        if media['type'] == 'animated_gif' and media_type != "video":
                            media_url = media['media_url_https']
                            media_type = 'photo'

                post_as_url = False

                if 'extended_entities' in data and 'media' in data['extended_entities']:
                    for media in data['extended_entities']['media']:
                        if media['type'] == 'photo' and not media_url:
                            media_url = media['media_url_https']
                            media_type = media['type']
                        if media['type'] == 'video':
                            post_as_url = True
                            media_type = media['type']
                        if media['type'] == 'animated_gif' and media_type != "video":
                            post_as_url = True
                            media_type = 'gif'

                if post_as_url:
                    text_variant = '[@%s](https://twitter.com/%s) tweeted (with %s) at %s: %s' %(data['user']['screen_name'], data['user']['screen_name'], media_type, datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y').isoformat(' '), "https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']))
                    wh = Webhook(url=wh_url, content=text_variant, username = username, icon_url=icon_url)
                    wh.post()
                    continue

                text = html.unescape(text)
                at = Embed(author_name=username,
                           author_url="https://twitter.com/" + data['user']['screen_name'],
                           author_icon=icon_url,
                           color=random.choice(colors),
                           description=text,
                           media_url=media_url,
                           media_type=media_type,
                           title=data['user']['name'],
                           url="https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']),
                           footer="Tweet created on",
                           footer_icon="https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png",
                           timestamp=datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y').isoformat(' '))


                print(strftime("[%Y-%m-%d %H:%M:%S]", gmtime()), data['user']['screen_name'], 'twittered.')

                wh = Webhook(url=wh_url, username = username, icon_url=icon_url)
                wh.addAttachment(at)


                if ('quoted_status' in data):


                    text = data['quoted_status']['text']
                    for url in data['quoted_status']['entities']['urls']:
                        if url['expanded_url'] == None:
                            continue
                        text = text.replace(url['url'], "[%s](%s)" % (url['display_url'], url['expanded_url']))

                    for userMention in data['quoted_status']['entities']['user_mentions']:
                        text = text.replace('@%s' %userMention['screen_name'], '[@%s](https://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))

                    text = html.unescape(text)
                    field = Field(data['quoted_status']['user']['screen_name'], text)
                    at.addField(field)
                wh.post()

        return True

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        print('on_limit')
        print(track)
        return

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print('on_error')
        print(status_code)
        return False

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice
        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        print('on_disconnect')
        print(notice)
        return

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print('on_warning')
        print(notice)
        return


if __name__ == '__main__':
    print('Bot started.')

    with open('data.json') as data_file:
        data = json.load(data_file)
        data_file.close()

    l = StdOutListener()
    auth = OAuthHandler(data['Twitter']['consumer_key'], data['Twitter']['consumer_secret'])
    auth.set_access_token(data['Twitter']['access_token'], data['Twitter']['access_token_secret'])
    stream = Stream(auth, l)

    print('Twitter stream started.')
    stream.filter(follow=data['twitter_ids'])
