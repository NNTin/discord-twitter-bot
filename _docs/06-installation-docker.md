---
title: "Docker"
permalink: /docs/inst-docker/
excerpt: "Docker Installation and Running"
toc: true
---

TODO:
Python installation.
Pip installation.
Requirements installation.
Link configuration methods.
Running the bot.

## Docker Setup
(**Warning:** This is only recommended for experienced users who have some basic experience with Docker.)

```bash
nano .env
docker run --env-file ./.env nntin/discord-twitter-bot
```

.env file example
```bash
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
