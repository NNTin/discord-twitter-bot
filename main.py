from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from discordWebhooks import Webhook, Attachment, Field
import calendar, time, random, configparser, json

#todo: add other games
#todo: make bot use default icon and username

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_status(self, status):
        """Called when a new status arrives"""

        colors = ['#7f0000', '#535900', '#40d9ff', '#8c7399', '#d97b6c', '#f2ff40', '#8fb6bf', '#502d59', '#66504d',
                  '#89b359', '#00aaff', '#d600e6', '#401100', '#44ff00', '#1a2b33', '#ff00aa', '#ff8c40', '#17330d',
                  '#0066bf', '#33001b', '#b39886', '#bfffd0', '#163a59', '#8c235b', '#8c5e00', '#00733d', '#000c59',
                  '#ffbfd9', '#4c3300', '#36d98d', '#3d3df2', '#590018', '#f2c200', '#264d40', '#c8bfff', '#f23d6d',
                  '#d9c36c', '#2db3aa', '#b380ff', '#ff0022', '#333226', '#005c73', '#7c29a6']

        try:
            data = status._json

            with open('data.json') as data_file:
                dataDiscords = json.load(data_file)

            for dataDiscord in dataDiscords['Discord']:

                if data['user']['id_str'] in dataDiscord[
                    'twitter_ids']:  # filter out tweets from people replying to dota 2 personalities

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

                        print(data['user']['screen_name'], ' twittered.')

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

        except:
            print('@@@@@@@@@@@@@@@@@@@@@@')
            print(data)
            print(type(data))

        return True


    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print('on_delete')
        print(status_id)
        print(user_id)
        return

    def on_event(self, status):
        """Called when a new event arrives"""
        print('on_event')
        print(status)
        return

    def on_direct_message(self, status):
        """Called when a new direct message arrives"""
        print('on_direct_message')
        print(status)
        return

    def on_friends(self, friends):
        """Called when a friends list arrives.
        friends is a list that contains user_id
        """
        print('on_friends')
        print(friends)
        return

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
    print('Starting bot....')

    with open('data.json') as data_file:
        data = json.load(data_file)

    l = StdOutListener()
    auth = OAuthHandler(data['Twitter']['consumer_key'], data['Twitter']['consumer_secret'])
    auth.set_access_token(data['Twitter']['access_token'], data['Twitter']['access_token_secret'])
    stream = Stream(auth, l)

    while True:
        try:
            stream.filter(follow=data['twitter_ids'])
        except:
            time.sleep(5)
            print('restarting')