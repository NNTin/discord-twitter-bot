# discord-twitter-bot
Post tweets to Discord Webhook of certain twitter users.  
Got questions? [Join the bot's discord server!](https://discord.gg/Dkg79tc)


## Preview

![](https://i.imgur.com/7Acpoo0.png)

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Remember to [activate](https://i.imgur.com/zOfa0Qm.png) the app. [View the logs here.](https://i.imgur.com/tWBoTuB.png)  
Use this to initially deploy your discord-twitter-bot.

To further configure the bot get Heroku CLI and run launcher.py.

```coffeescript
heroku login
heroku git:clone -a <your heroku app name>
cd <your heroku app name>
git remote add origin https://github.com/NNTin/discord-twitter-bot
git pull origin master
python3 launcher.py
git add .
git commit -am "updated configuration"
git push heroku
```

Heroku is a nice solution to host the bot for free.

## YT Video to Heroku Deployment

[![YT Video](https://img.youtube.com/vi/NwPcXBvStSI/0.jpg)](https://www.youtube.com/watch?v=NwPcXBvStSI)

## Normal Setup

Get Python >=3.5.3, <3.7

```coffeescript
python3 -m venv bot-env
source bot-env/bin/activate
git clone https://github.com/NNTin/discord-twitter-bot.git
python3 discord-twitter-bot/launcher.py
```

First two lines are skip-able but are recommended if you are relying on an older version of discord.py.
Third line clones the rewrite branch. Fourth line executes launcher.py

Once you have set everything up you can run main.py directly. (Useful in combination with systemd, Upstart, PM2, etc.)

![](https://i.imgur.com/TdJahu9.png)

Useful links:
* [Twitter API](https://developer.twitter.com/en/apps)
* [What's a webhook?](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)


## Credits
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members).  
JacobWolf for providing the [twitter lists](https://twitter.com/JacobWolf/lists) for CS:GO, LoL, Overwatch, CoD and SSMB.
