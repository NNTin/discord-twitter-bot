import unittest
from bot.utils.processor import worth_posting, keyword_set_present


class TestOptions(unittest.TestCase):
    def test_worth_posting1(self):
        self.assertFalse(
            worth_posting(
                tweeter_id="000",
                twitter_ids=["123", "456"],
                in_reply_to_twitter_id="789",
                retweeted=True,
                include_reply_to_user=True,
                include_user_reply=True,
                include_retweet=True,
            ),
            "Tracked twitter id is not in the tracked list, nor is tracked twitter id being mentioned in a reply.",
        )

    def test_worth_posting2(self):
        self.assertFalse(
            worth_posting(
                tweeter_id="123",
                twitter_ids=["123", "456"],
                in_reply_to_twitter_id="789",
                retweeted=True,
                include_reply_to_user=True,
                include_user_reply=False,
                include_retweet=True,
            ),
            "include_user_reply is false as such in_reply_to_twitter_id should be None",
        )

    def test_worth_posting3(self):
        self.assertFalse(
            worth_posting(
                tweeter_id="789",
                twitter_ids=["123", "456"],
                in_reply_to_twitter_id="123",
                retweeted=True,
                include_reply_to_user=False,
                include_user_reply=True,
                include_retweet=True,
            ),
            "include_reply_to_user is false as such the tweet will be ignored",
        )

    def test_worth_posting4(self):
        self.assertTrue(
            worth_posting(
                tweeter_id="123",
                twitter_ids=["123", "456"],
                in_reply_to_twitter_id=None,
                retweeted=False,
                include_reply_to_user=False,
                include_user_reply=False,
                include_retweet=False,
            ),
            "Tweeter is in tracked twitter list, not replying to anyone, not a retweeted status",
        )

    def test_worth_posting5(self):
        self.assertFalse(
            worth_posting(
                tweeter_id="123",
                twitter_ids=["123", "456"],
                in_reply_to_twitter_id=None,
                retweeted=True,
                include_reply_to_user=True,
                include_user_reply=True,
                include_retweet=False,
            ),
            "include_retweet is false meaning retweets are ignored",
        )

    def test_keyword_sets_present1(self):
        self.assertTrue(
            keyword_set_present([[""]], "Hello World!"),
            "Expecting true when no keyword set was supplied.",
        )

    def test_keyword_set_present2(self):
        self.assertTrue(keyword_set_present([["world"]], "Hello World!"), "Keyword present!")

    def test_keyword_set_present3(self):
        self.assertTrue(
            keyword_set_present([["hello", "world"]], "Hello World!"), "Keyword set present!"
        )

    def test_keyword_set_present4(self):
        self.assertTrue(
            keyword_set_present([["bye"], ["world"]], "Hello World!"), "Keyword present!"
        )

    def test_keyword_set_present5(self):
        self.assertFalse(
            keyword_set_present([["hello", "nntin"]], "Hello World!"), "Keyword set not present"
        )

    def test_keyword_set_present6(self):
        self.assertTrue(
            keyword_set_present([["bye", "world"], ["hello"]], "Hello World!"), "Keyword present!"
        )
