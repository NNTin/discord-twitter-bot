from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from tweepy.api import API
from discordWebhooks import Webhook, Attachment, Field
import calendar, time, random, json
from time import gmtime, strftime

#todo: fix & < and > see: https://api.slack.com/docs/message-formatting


class StdOutListener(StreamListener):
    def __init__(self, api=None):
        self.api = api or API()


    def on_status(self, status):
        """Called when a new status arrives"""

        colors = ['#7f0000', '#535900', '#40d9ff', '#8c7399', '#d97b6c', '#f2ff40', '#8fb6bf', '#502d59', '#66504d',
                  '#89b359', '#00aaff', '#d600e6', '#401100', '#44ff00', '#1a2b33', '#ff00aa', '#ff8c40', '#17330d',
                  '#0066bf', '#33001b', '#b39886', '#bfffd0', '#163a59', '#8c235b', '#8c5e00', '#00733d', '#000c59',
                  '#ffbfd9', '#4c3300', '#36d98d', '#3d3df2', '#590018', '#f2c200', '#264d40', '#c8bfff', '#f23d6d',
                  '#d9c36c', '#2db3aa', '#b380ff', '#ff0022', '#333226', '#005c73', '#7c29a6']

        data = status._json
        print(data)

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


                wh = Webhook(url=wh_url)

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
                    text = text.replace('@%s' %userMention['screen_name'], '[@%s](http://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))

                media_url = ''
                if 'extended_tweet' in data:
                    if 'media' in data['extended_tweet']['entities']:
                        for media in data['extended_tweet']['entities']['media']:
                            if media['type'] == 'photo':
                                media_url = media['media_url']

                if 'media' in data['entities']:
                    for media in data['entities']['media']:
                        if media['type'] == 'photo':
                            media_url = media['media_url']


                at = Attachment(author_name=data['user']['screen_name'],
                                author_icon=data['user']['profile_image_url'],
                                color=random.choice(colors), pretext=text,
                                image_url=media_url,
                                title_link="https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']),
                                footer="Tweet created on",
                                footer_icon="https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png",
                                ts=calendar.timegm(time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')))


                print(strftime("[%Y-%m-%d %H:%M:%S]", gmtime()), data['user']['screen_name'], 'twittered.')

                wh.addAttachment(at)


                if ('quoted_status' in data):


                    text = data['quoted_status']['text']
                    for url in data['quoted_status']['entities']['urls']:
                        if url['expanded_url'] == None:
                            continue
                        text = text.replace(url['url'], "[%s](%s)" % (url['display_url'], url['expanded_url']))

                    for userMention in data['quoted_status']['entities']['user_mentions']:
                        text = text.replace('@%s' %userMention['screen_name'], '[@%s](http://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))



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





    while True:
        try:
            print('Twitter stream started.')
            stream.filter(follow=data['twitter_ids'])
        except:
            time.sleep(5)
            print('restarting')
