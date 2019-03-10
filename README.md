<h1 align="center">discord-twitter-bot</h1>
<p align="center">Posts Twitter Tweets to Discord through Webhook</p>

<p align="center">
  <a href="https://discord.gg/Dkg79tc"><img alt="Invite Link" src="https://discordapp.com/api/guilds/295528852518731786/widget.png?style=shield"></a>
  <a href="https://github.com/nntin/discord-twitter-bot/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-brightgreen.svg"></a>
  <a href="https://travis-ci.com/NNTin/discord-twitter-bot"><img alt="Build Status" src="https://api.travis-ci.com/NNTin/discord-twitter-bot.svg"></a>
  <a href="https://github.com/nntin/discord-twitter-bot"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://github.com/NNTin/discord-twitter-bot/commits/"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/nntin/discord-twitter-bot.svg"></a>
  <a href="https://github.com/NNTin/discord-twitter-bot/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/nntin/discord-twitter-bot.svg"></a>
  <a href="https://hub.docker.com/r/nntin/discord-twitter-bot"><img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/nntin/discord-twitter-bot.svg"></a>
</p>

## Preview
[![](img/gif.gif)](https://discord.gg/Dkg79tc)

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Remember to [activate](https://i.imgur.com/zOfa0Qm.png) the app. [View the logs here.](https://i.imgur.com/tWBoTuB.png)  
Use this to initially deploy your discord-twitter-bot.

To further configure the bot get Heroku CLI and run launcher.py. (**Warning:** This is not recommended for inexperienced users since a lot of things could go wrong.)

```coffeescript
heroku login
heroku create <your heroku app name>
cd <your heroku app name>
git remote add origin https://github.com/NNTin/discord-twitter-bot
git pull origin master
python bot/launcher.py
git add .
git commit -am "updated configuration"
git push heroku
```

This will create a data.json and the bot will ignore any set environment variable.

## YT Video to Heroku Deployment

[![YT Video](https://img.youtube.com/vi/NwPcXBvStSI/0.jpg)](https://www.youtube.com/watch?v=NwPcXBvStSI)

## Docker Setup
(**Warning:** This is only recommended for experienced users who have some basic experience with Docker.)

```bash
nano .env
docker run --env-file ./.env nntin/discord-twitter-bot
```

.env file example
```
ACCESS_TOKEN=XXX-XXX
ACCESS_TOKEN_SECRET=XXX
CONSUMER_KEY=XXX
CONSUMER_SECRET=XXX
TWITTER_ID=123,456,789
TWITTER_LIST=https://twitter.com/rokxx/lists/dota-2
TWITTER_HANDLE=discordapp
WEBHOOK_URL=https://discordapp.com/api/webhooks/123456789/XXXX-XXXX
```

Optional environment variables: `INCLUDE_REPLY_TO_USER`, `INCLUDE_RETWEET`, `INCLUDE_USER_REPLY`, `CUSTOM_MESSAGE`, `KEYWORDS`

One of the 3 environment variables are required: `TWITTER_ID`, `TWITTER_LIST` and `TWITTER_HANDLE`. You can specify all three.

## Normal Setup
(**Warning:** This is only recommended for experienced users who have some basic experience with CLI.)

Get Python >=3.6.0

```
git clone https://github.com/NNTin/discord-twitter-bot.git
cd discord-twitter-bot      # ^ download the project and cd into it
python3 -m venv venv        # optional virtual environment, recommended
source venv/bin/activate    # only run if you did venv
python3 bot/launcher.py     # configure the bot, this create a config.json
python3 bot/main.py         # run the bot
```

Once you have set everything up you can run main.py directly. (Useful in combination with systemd, Upstart, PM2, etc.)

![](https://i.imgur.com/TdJahu9.png)

Useful links:
* [Twitter API](https://developer.twitter.com/en/apps)
* [What's a webhook?](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

##  Why?
Q: Why Heroku?  
A: Heroku has a lot of bad reputation for being an inferior hosting service. The heroku dynos restart roughly every 24 hours and data are lost. However Heroku can be incredibly user friendly once it is properly set up. No knowledge about git, ssh and python is required. I personally don't host anything on Heroku but I appreciate Heroku since it is a free hosting solution and it can be very user friendly (but not developer friendly).

Q: Why add automated testing and automated docker image deployment for a relatively simple solo project? Isn't this overkill?  
A: Continuous integration/deployment is incredible useful in bigger projects. It cuts down development time. I contributed to other FOSS projects that had CI/CD and I was interested how the flow was actually implemented.

Q: Why Travis and Azure Pipelines?  
I added Travis CI support first. [But then I learned about how they were acquired by another company and there was a massive layoff.](https://twitter.com/carmatrocity/status/1098538649908666368) I then looked for alternatives in case the Travis becomes less user friendly and Azure Pipelines seemed like a good choice. I have migrated from Travis to Azure Pipelines but I will keep both around for educational purposes.


## Credits
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members).  
JacobWolf for providing the [twitter lists](https://twitter.com/JacobWolf/lists) for CS:GO, LoL, Overwatch, CoD and SSMB.
