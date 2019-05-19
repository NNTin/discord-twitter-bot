import json
from jsonschema import validate
import unittest
from bot.config import config
import os


def read_json(filename):
    with open(filename, encoding="utf-8", mode="r") as f:
        data = json.load(f)
    return data


class TestConfig(unittest.TestCase):
    def test_validate_json(self):
        os.chdir(os.path.dirname(__file__))
        schema = read_json("config_schema.json")
        self.assertIsNone(validate(config, schema), "JSON Validation passed.")

    def test_location_validation(self):
        for d in config["Discord"]:
            self.assertTrue(len(d.get("location", [])) % 4 == 0)
