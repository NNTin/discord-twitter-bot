from html import unescape
import re
from discord import Webhook, RequestsWebhookAdapter, Embed
import discord
import random
from datetime import datetime


COLORS = [0x7f0000, 0x535900, 0x40d9ff, 0x8c7399, 0xd97b6c, 0xf2ff40, 0x8fb6bf, 0x502d59, 0x66504d,
          0x89b359, 0x00aaff, 0xd600e6, 0x401100, 0x44ff00, 0x1a2b33, 0xff00aa, 0xff8c40, 0x17330d,
          0x0066bf, 0x33001b, 0xb39886, 0xbfffd0, 0x163a59, 0x8c235b, 0x8c5e00, 0x00733d, 0x000c59,
          0xffbfd9, 0x4c3300, 0x36d98d, 0x3d3df2, 0x590018, 0xf2c200, 0x264d40, 0xc8bfff, 0xf23d6d,
          0xd9c36c, 0x2db3aa, 0xb380ff, 0xff0022, 0x333226, 0x005c73, 0x7c29a6]
WH_REGEX = r"discordapp\.com\/api\/webhooks\/(?P<id>\d+)\/(?P<token>.+)"


def worth_posting(tweeter_id, twitter_ids, in_reply_to_twitter_id, retweeted,
                  include_reply_to_user, include_user_reply, include_retweet):
    if tweeter_id not in twitter_ids:
        worth_posting = False
        if include_reply_to_user:
            if in_reply_to_twitter_id in twitter_ids:
                worth_posting = True
    else:
        worth_posting = True
        if not include_user_reply and in_reply_to_twitter_id is not None:
            worth_posting = False

    if not include_retweet:
        if retweeted:
            worth_posting = False
    return worth_posting


def keyword_set_present(keyword_sets, text):
    for keyword_set in keyword_sets:
        keyword_present = [keyword.lower() in text.lower() for keyword in keyword_set]
        keyword_set_present = all(keyword_present)
        if keyword_set_present:
            return True
    return False


class Processor:
    def __init__(self, status_tweet, discord_config):
        self.status_tweet = status_tweet
        self.discord_config = discord_config
        self.text = ""
        self.embed = None

    def worth_posting(self):
        return worth_posting(
            tweeter_id=self.status_tweet["user"]["id_str"],
            twitter_ids=self.discord_config["twitter_ids"],
            in_reply_to_twitter_id=self.status_tweet["in_reply_to_user_id_str"],
            retweeted=self.status_tweet["retweeted"],
            include_reply_to_user=self.discord_config["IncludeReplyToUser"],
            include_user_reply=self.discord_config["IncludeUserReply"],
            include_retweet=self.discord_config["IncludeRetweet"]
        )

    def get_text(self):
        if 'extended_tweet' in self.status_tweet:
            self.text = self.status_tweet['extended_tweet']['full_text']
        elif 'full_text' in self.status_tweet:
            self.text = self.status_tweet['full_text']
        else:
            self.text = self.status_tweet['text']

        for url in self.status_tweet['entities']['urls']:
            if url['expanded_url'] is None:
                continue
            self.text = self.text.replace(url['url'], "[%s](%s)" % (url['display_url'], url['expanded_url']))

        for userMention in self.status_tweet['entities']['user_mentions']:
            self.text = self.text.replace('@%s' % userMention['screen_name'],
                                          '[@%s](https://twitter.com/%s)' % (userMention['screen_name'],
                                                                             userMention['screen_name']))

        if 'extended_tweet' in self.status_tweet:
            for hashtag in sorted(self.status_tweet['extended_tweet']['entities']["hashtags"], key=lambda k: k["text"],
                                  reverse=True):
                self.text = self.text.replace('#%s' % hashtag['text'],
                                              '[#%s](https://twitter.com/hashtag/%s)' % (hashtag['text'],
                                                                                         hashtag['text']))

        for hashtag in sorted(self.status_tweet['entities']["hashtags"], key=lambda k: k["text"],
                              reverse=True):
            self.text = self.text.replace('#%s' % hashtag['text'],
                                          '[#%s](https://twitter.com/hashtag/%s)' % (hashtag['text'],
                                                                                     hashtag['text']))
        return unescape(self.text)

    def keyword_set_present(self):
        return keyword_set_present(self.discord_config["keyword_sets"], self.text)

    def attach_media(self):
        if 'extended_tweet' in self.status_tweet and 'media' in self.status_tweet['extended_tweet']['entities']:
            for media in self.status_tweet['extended_tweet']['entities']['media']:
                if media['type'] == 'photo':
                    self.embed.set_image(url=media['media_url_https'])
                elif media['type'] == 'video':
                    pass
                elif media['type'] == 'animated_gif':
                    pass

        if 'media' in self.status_tweet['entities']:
            for media in self.status_tweet['entities']['media']:
                if media['type'] == 'photo':
                    self.embed.set_image(url=media['media_url_https'])
                elif media['type'] == 'video':
                    pass
                elif media['type'] == 'animated_gif':
                    pass

        if 'extended_entities' in self.status_tweet and 'media' in self.status_tweet['extended_entities']:
            for media in self.status_tweet['extended_entities']['media']:
                if media['type'] == 'photo':
                    self.embed.set_image(url=media['media_url_https'])
                elif media['type'] == 'video':
                    pass
                elif media['type'] == 'animated_gif':
                    pass

    def create_embed(self):
        self.embed = Embed(colour=random.choice(COLORS),
                           url='https://twitter.com/{}/status/{}'.format(self.status_tweet['user']['screen_name'],
                                                                         self.status_tweet['id_str']),
                           title=self.status_tweet['user']['name'],
                           description=self.text,
                           timestamp=datetime.strptime(self.status_tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

        self.embed.set_author(name=self.status_tweet['user']['screen_name'],
                              url="https://twitter.com/" + self.status_tweet['user']['screen_name'],
                              icon_url=self.status_tweet['user']['profile_image_url'])
        self.embed.set_footer(text='Tweet created on',
                              icon_url='https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png')

    def send_message(self, wh_url):
        match = re.search(WH_REGEX, wh_url)

        if match:
            webhook = Webhook.partial(int(match.group("id")), match.group("token"), adapter=RequestsWebhookAdapter())
            try:
                if "custom_message" in self.discord_config and self.discord_config["custom_message"] is not None:
                    webhook.send(embed=self.embed, content=self.discord_config["custom_message"])
                else:
                    webhook.send(embed=self.embed)
            except discord.errors.NotFound as error:
                print(f"---------Error---------\n"
                      f"discord.errors.NotFound\n"
                      f"The Webhook does not exist."
                      f"{error}\n"
                      f"-----------------------")
            except discord.errors.Forbidden as error:
                print(f"---------Error---------\n"
                      f"discord.errors.Forbidden\n"
                      f"The authorization token of your Webhook is incorrect."
                      f"{error}\n"
                      f"-----------------------")
            except discord.errors.InvalidArgument as error:
                print(f"---------Error---------\n"
                      f"discord.errors.InvalidArgument\n"
                      f"You modified the code. You can't mix embed and embeds."
                      f"{error}\n"
                      f"-----------------------")
            except discord.errors.HTTPException as error:
                print(f"---------Error---------\n"
                      f"discord.errors.HTTPException\n"
                      f"Your internet connection is whack."
                      f"{error}\n"
                      f"-----------------------")
        else:
            print(f"---------Error---------\n"
                  f"The following webhook URL is invalid:\n"
                  f"{wh_url}\n"
                  f"-----------------------")


if __name__ == '__main__':
    p = Processor({}, {"keyword_sets": [[""]]})
    p.text = "Hello World!"
    print(p.keyword_set_present())

