import discord
import unittest


class TestWebhook(unittest.TestCase):
    def test_discord(self):
        self.assertEqual(
            discord.version_info.major,
            1,
            msg="discord.py rewrite (>=1.0.0) is needed. "
            "You have {}.{}.{}".format(*discord.version_info[:3]),
        )
