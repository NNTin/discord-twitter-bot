from bot.config import config
from bot.utils.twitter_id_converter import Converter
import tweepy
import unittest


class TestTwitter(unittest.TestCase):
    def setUp(self):
        self.auth = tweepy.OAuthHandler(
            config["Twitter"]["consumer_key"], config["Twitter"]["consumer_secret"]
        )
        self.auth.set_access_token(
            config["Twitter"]["access_token"], config["Twitter"]["access_token_secret"]
        )
        self.client = tweepy.API(self.auth)

    def test_login(self):
        self.client.verify_credentials()

    def test_valid_twitter_ids(self):
        c = Converter(config, self.auth)
        c.convert()
