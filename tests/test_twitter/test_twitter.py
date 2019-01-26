from bot.config import config
import tweepy
import unittest


class TestTwitter(unittest.TestCase):
    def test_login(self):
        auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'])
        auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])
        client = tweepy.API(auth)
        client.verify_credentials()

    def test_valid_twitter_ids(self):
        def lookup_users_list(_twitter_ids):
            full_users = []
            user_count = len(_twitter_ids)
            while True:
                for i in range(0, int((user_count // 100)) + 1):
                    try:
                        full_users.extend(
                            client.lookup_users(user_ids=_twitter_ids[i * 100:min((i + 1) * 100, user_count)]))
                    except:
                        raise Exception("Invalid twitter IDs")
                return full_users

        twitter_ids = []
        for element in config['Discord']:
            twitter_ids.extend(x for x in element['twitter_ids'] if x not in twitter_ids)

        auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'])
        auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])
        client = tweepy.API(auth)
        client.verify_credentials()

        valid_twitter_ids = []

        user_objs = lookup_users_list(twitter_ids)

        for user in user_objs:
            print('twitter id: {} -> screen name: {}'.format(user.id, user.screen_name))
            valid_twitter_ids.append(str(user.id))

        self.assertEqual(len(twitter_ids), len(valid_twitter_ids),
                         f"Of the {len(twitter_ids)} twitter ids only {len(valid_twitter_ids)} were valid.")
