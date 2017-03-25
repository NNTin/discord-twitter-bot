#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from discordWebhooks import Webhook, Attachment, Field
import calendar, time, secret, random

followedTwitterIDs = ['3065618342']
colors = ['#7f0000', '#535900', '#40d9ff', '#8c7399', '#d97b6c', '#f2ff40', '#8fb6bf', '#502d59', '#66504d', '#89b359', '#00aaff', '#d600e6', '#401100', '#44ff00', '#1a2b33', '#ff00aa', '#ff8c40', '#17330d', '#0066bf', '#33001b', '#b39886', '#bfffd0', '#163a59', '#8c235b', '#8c5e00', '#00733d', '#000c59', '#ffbfd9', '#4c3300', '#36d98d', '#3d3df2', '#590018', '#f2c200', '#264d40', '#c8bfff', '#f23d6d', '#d9c36c', '#2db3aa', '#b380ff', '#ff0022', '#333226', '#005c73', '#7c29a6']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_status(self, status):
        """Called when a new status arrives"""
        try:
            data = status._json

            sendIt = False

            wh = Webhook(url=secret.WEBHOOK_URL, username="Chirp",
                         icon_url="http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_lg.png")
            if data['user']['id_str'] in followedTwitterIDs or data['user']['id_str'] not in followedTwitterIDs: #filter out random people replying to Dota 2 personalities
                text = data['text']
                for url in data['entities']['urls']:
                    if url['expanded_url'] == None:
                        continue
                    text = text.replace(url['url'], "[%s](%s)" %(url['display_url'],url['expanded_url']))
                at = Attachment(author_name=data['user']['screen_name'],
                                author_icon=data['user']['profile_image_url'],
                                color=random.choice(colors), pretext=text,
                                title_link="https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']),
                                footer="Tweet created at",
                                footer_icon="https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png",
                                ts=calendar.timegm(time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')))
                wh.addAttachment(at)


            #if ('retweeted_status' in data): #not reliable. Twitter data is not consistent.
            if ('quoted_status' in data):

                print(data)

                text = data['quoted_status']['text']
                for url in data['quoted_status']['entities']['urls']:
                    if url['expanded_url'] == None:
                        continue
                    text = text.replace(url['url'], "[%s](%s)" % (url['display_url'], url['expanded_url']))


                field = Field(data['quoted_status']['user']['screen_name'], text)
                at.addField(field)


                sendIt = True




            if (sendIt):
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

    l = StdOutListener()
    auth = OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
    auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['soccer', 'basketball'])
    while True:
        try:
            #stream.filter(follow=followedTwitterIDs)
            stream.filter(track=['soccer', 'basketball'])
        except:
            time.sleep(5)
            print('restarting')