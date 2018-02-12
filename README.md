# discord-twitter-bot
Post tweets to Discord Webhook of certain twitter users.  
Got questions? [Join the bot's discord server!](https://discord.gg/Dkg79tc)

This rewrite branch uses the rewrite version of discord.py which is in beta.

## Preview

[![](img/gif.gif)](https://discord.gg/Dkg79tc)

## Setup

**You need to host this bot yourself.**

Get Python 3.5 or later.

```python
python3 -m venv bot-env
source bot-env/bin/activate
python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py
git clone -b rewrite --single-branch https://github.com/NNTin/discord-twitter-bot.git
cd discord-twitter-bot
python3 launcher.py
```

Creating a virtual environment and activating it. You can skip this but it is recommended if you are relying on an older version of discord.py.
Installing the rewrite version of discord.py.
Git cloning the rewrite branch of this GitHub project
Executing launcher.py

Once you have set everything up you can start main.py directly.


![](https://i.imgur.com/TdJahu9.png)

Useful links:
* [Twitter API](https://apps.twitter.com/)
* [What's a webhook?](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Credits
Derpolino for providing the [discord-webhook-python](https://github.com/Derpolino/discord-webhooks-python) code.
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members).
JacobNWolf for providing the [twitter lists](https://twitter.com/JacobNWolf/lists/) for CS:GO, LoL, Overwatch, CoD and SSMB.