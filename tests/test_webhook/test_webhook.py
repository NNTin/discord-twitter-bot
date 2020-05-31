from bot.config import config
import unittest
import requests


class TestWebhook(unittest.TestCase):
    def test_webhook(self):
        r = [
            [requests.get(wh_url).status_code for wh_url in discord.get("webhook_urls", [])]
            for discord in config["Discord"]
        ]
        for arr in r:
            for ele in arr:
                self.assertEqual(ele, 200, "Webhook URL faulty.")
