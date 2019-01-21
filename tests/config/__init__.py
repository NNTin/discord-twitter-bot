import json
from jsonschema import validate

config = {
    "Discord": [
        {
            "custom_message": "Pinging <@1234567890>",
            "keyword_sets": [
            ],
            "IncludeReplyToUser": False,
            "IncludeRetweet": False,
            "IncludeUserReply": False,
            "twitter_ids": [
                "5646464654"
            ],
            "webhook_urls": [
                "https://ptb.discordapp.com/api/webhooks/1234567890/XXXXXXXXXXXXXXXXXXXXXXXXXX"
            ]
        }
    ],
    "Twitter": {
        "access_token": "X-X",
        "access_token_secret": "X",
        "consumer_key": "X",
        "consumer_secret": "X"
    }
}


def read_json(filename):
    with open(filename, encoding='utf-8', mode="r") as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    schema = read_json("config_schema.json")
    print(schema)
    validate(config, schema)
