#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from discordWebhooks import Webhook, Attachment, Field
import calendar, time, secret

followedTwitterIDs = ['3065618342']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_status(self, status):
        """Called when a new status arrives"""
        try:
            data = status._json
            print(data)
            if data['user']['id_str'] in followedTwitterIDs or data['user']['id_str'] not in followedTwitterIDs: #filter out random people replying to Dota 2 personalities

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