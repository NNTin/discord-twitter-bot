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


            if data['user']['id_str'] in dataDiscord['twitter_ids'] or data['in_reply_to_user_id_str'] in dataDiscord['twitter_ids']:
                print(data)

            data = {'created_at': 'Mon Oct 09 00:53:41 +0000 2017', 'id': 917191302118203392, 'id_str': '917191302118203392', 'text': '@Twitch can someone look into markdowns not working plz? Makin my channel look like a chump rn https://t.co/XLrYoVwGyr', 'display_text_range': [0, 94], 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': 309366491, 'in_reply_to_user_id_str': '309366491', 'in_reply_to_screen_name': 'Twitch', 'user': {'id': 821802513758232577, 'id_str': '821802513758232577', 'name': 'Nikkiduhgames', 'screen_name': 'NikkiDuhGames', 'location': 'Turn post notifications on!', 'url': 'http://www.twitch.tv/nikkiduhgames', 'description': 'Video game master, beer chuggin, bartender and dog crazed Virgo 🖖 @twitchkittens', 'translator_type': 'none', 'protected': False, 'verified': False, 'followers_count': 1907, 'friends_count': 2098, 'listed_count': 10, 'favourites_count': 1749, 'statuses_count': 1276, 'created_at': 'Wed Jan 18 19:32:42 +0000 2017', 'utc_offset': -25200, 'time_zone': 'Pacific Time (US & Canada)', 'geo_enabled': False, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_link_color': 'F58EA8', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/881617627092733952/8bLKakMA_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/881617627092733952/8bLKakMA_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/821802513758232577/1499098249', 'default_profile': False, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'quote_count': 0, 'reply_count': 0, 'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [], 'urls': [], 'user_mentions': [{'screen_name': 'Twitch', 'name': 'Twitch', 'id': 309366491, 'id_str': '309366491', 'indices': [0, 7]}], 'symbols': [], 'media': [{'id': 917191291489763329, 'id_str': '917191291489763329', 'indices': [95, 118], 'media_url': 'http://pbs.twimg.com/tweet_video_thumb/DLqEnsBUQAEdA9w.jpg', 'media_url_https': 'https://pbs.twimg.com/tweet_video_thumb/DLqEnsBUQAEdA9w.jpg', 'url': 'https://t.co/XLrYoVwGyr', 'display_url': 'pic.twitter.com/XLrYoVwGyr', 'expanded_url': 'https://twitter.com/NikkiDuhGames/status/917191302118203392/photo/1', 'type': 'photo', 'sizes': {'large': {'w': 320, 'h': 400, 'resize': 'fit'}, 'small': {'w': 320, 'h': 400, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 320, 'h': 400, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 917191291489763329, 'id_str': '917191291489763329', 'indices': [95, 118], 'media_url': 'http://pbs.twimg.com/tweet_video_thumb/DLqEnsBUQAEdA9w.jpg', 'media_url_https': 'https://pbs.twimg.com/tweet_video_thumb/DLqEnsBUQAEdA9w.jpg', 'url': 'https://t.co/XLrYoVwGyr', 'display_url': 'pic.twitter.com/XLrYoVwGyr', 'expanded_url': 'https://twitter.com/NikkiDuhGames/status/917191302118203392/photo/1', 'type': 'animated_gif', 'sizes': {'large': {'w': 320, 'h': 400, 'resize': 'fit'}, 'small': {'w': 320, 'h': 400, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 320, 'h': 400, 'resize': 'fit'}}, 'video_info': {'aspect_ratio': [4, 5], 'variants': [{'bitrate': 0, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/tweet_video/DLqEnsBUQAEdA9w.mp4'}]}}]}, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'filter_level': 'low', 'lang': 'en', 'timestamp_ms': '1507510421672'}


            worthPosting = True

            if data['user']['id_str'] not in dataDiscord['twitter_ids']:
                worthPosting = False
                if 'IncludeReplyToUser' in dataDiscord:     #other Twitter user tweeting to your followed Twitter user
                    if dataDiscord['IncludeUserReply'] == True:
                        if data['in_reply_to_user_id_str'] in dataDiscord['twitter_ids']:
                            worthPosting = True
            else:
                worthPosting = True
                if 'IncludeUserReply' in dataDiscord:  # your followed Twitter users tweeting to random Twitter users (relevant if you only want status updates/opt out of conversations)
                    if dataDiscord['IncludeUserReply'] == False and data['in_reply_to_user_id'] is not None:
                            worthPosting = False


            if not worthPosting:
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
                    print(strftime("[%Y-%m-%d %H:%M:%S]", gmtime()), data['user']['screen_name'], 'twittered. [Path 2]')

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
