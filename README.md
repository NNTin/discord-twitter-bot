# discord-twitter-bot
Post tweets to Discord Webhook. It can be filtered by tracking keywords or by following twitter users.

## Preview
![](https://i.imgur.com/a4Sf3vE.png)

## TODOs
### Neater formatting on discord text channel
- [x] If is_quote_status: add Field containing the quoted status
- [x] If retweeted: identify it as a retweet
- [x] If picture(s) provided: send pictures in into text channel
### Core
- [x] use [default on_data()](https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py#L45)
- [x] handle tweets in on_status()
- [ ] twitter id converter (in the meantime use [this](http://gettwitterid.com/))
- [x] extract twitter IDs from dota 2 personalities
### Make it easier to use
- [x] config file with config.example instead of secret.py
- [ ] discord-twitter-bot Wiki
- [x] setupBot.py file for easier setting up

## Credits
Derpolino for providing the [discord-webhook-python](https://github.com/Derpolino/discord-webhooks-python) code.
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members)