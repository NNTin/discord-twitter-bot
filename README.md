# discord-twitter-bot
Post tweets to Discord Webhook of certain twitter users.  
Got questions? [Join the bot's discord server!](https://discord.gg/Dkg79tc)

This rewrite branch uses the rewrite version of discord.py which is in beta.
Warning: If you are relying on the async version of discord.py use Python's virtual environment. 
Not using venv will break your other projects.

## Preview

[![](img/gif.gif)](https://discord.gg/Dkg79tc)

## Setup

**You need to host this bot yourself.**

Get Python 3.5 or later.

```coffeescript
python3 -m venv bot-env
source bot-env/bin/activate
git clone -b rewrite --single-branch https://github.com/NNTin/discord-twitter-bot.git
python3 discord-twitter-bot/launcher.py
```

First two lines are skip-able but are recommended if you are relying on an older version of discord.py.
Third line clones the rewrite branch. Fourth line executes launcher.py

Once you have set everything up you can start main.py directly.


![](https://i.imgur.com/TdJahu9.png)

Useful links:
* [Twitter API](https://apps.twitter.com/)
* [What's a webhook?](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Credits
Derpolino for providing the [discord-webhook-python](https://github.com/Derpolino/discord-webhooks-python) code.  
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members).  
JacobNWolf for providing the [twitter lists](https://twitter.com/JacobNWolf/lists/) for CS:GO, LoL, Overwatch, CoD and SSMB.