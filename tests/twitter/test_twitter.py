from bot.config import config
import tweepy
import unittest


class TestTwitter(unittest.TestCase):
    def test_login(self):
        auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'])
        auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])
        client = tweepy.API(auth)
        client.verify_credentials()
