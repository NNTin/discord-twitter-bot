# discord-twitter-bot
Post tweets to Discord Webhook. It can be filtered by tracking keywords or by following twitter users.

## Preview
![](http://i.imgur.com/gy4dz9L.png)

## TODOs
### Neater formatting on discord text channel
- [x] If is_quote_status: add Field containing the quoted status
- [x] If retweeted: identify it as a retweet
- [ ] If picture(s) provided: send pictures in into text channel
### Core
- [x] use [default on_data()](https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py#L45)
- [x] handle tweets in on_status()
- [ ] utilize on_connect(), on_event(), on_direct_message(), etc.
- [ ] twitter handle to twitter id converter
- [x] extract twitter IDs from [rokxx's dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members)
### Make it easier to use
- [ ] config file with config.example instead of secret.py
- [ ] discord-twitter-bot Wiki
- [ ] setup.py file for easier setting up
- [ ] run.sh file for one click executing (once configured)

## Credits
Derpolino for providing the [discord-webhook-python](https://github.com/Derpolino/discord-webhooks-python) code.
