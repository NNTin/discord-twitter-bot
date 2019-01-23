from bot.config import config
import discord
import unittest
import requests


class TestWebhook(unittest.TestCase):
    def test_discord(self):
        self.assertEqual(
            discord.version_info.major, 1,
            msg="discord.py rewrite (>=1.0.0) is needed. "
                "You have {}.{}.{}".format(*discord.version_info[:3])
        )

    def test_webhook(self):
        r = [[requests.get(wh_url).status_code for wh_url in discord["webhook_urls"]] for discord in config["Discord"]]
        for arr in r:
            for ele in arr:
                self.assertEqual(ele, 200, "Webhook URL faulty.")


if __name__ == '__main__':
    t = TestWebhook()
    t.test_discord()
