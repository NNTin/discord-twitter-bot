# discord-twitter-bot
Post tweets to Discord Webhook of certain twitter users.  
Got questions? [Join the bot's discord server!](https://discord.gg/Dkg79tc)

## Preview

[<img src="/img/gif.gif?raw=true" width="840px">](https://discord.gg/Dkg79tc)

## New Launcher

I have now added an experimental launcher file. From which you can setup the bot as well as run the bot. Please provide feedback. In the near future I will delete the old setup files since they've become obsolete.

With the new launcher file it is easier to add/remove webhook. You don't need to enter your Twitter credentials each time. And it provides some troubleshooting messages.

The majority of problems users had came from the setup file. This should alleviate the problem.

Get Python 3.5 or later and run launcher.py

## Old Setup (soon to be deprecated)

* The bot is written in Python3 and requires tweepy.
* Create a data.json file by executing setupBot.py.
* There it will ask for Twitter API keys&secret as well as access token&secret. You can get it [here](https://apps.twitter.com/).
* You need a Discord Webhook URL. See [this intro](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for a detailed explanation.
* Lastly it will ask for Twitter **IDs** or a Twitter **List** URL depending on the setupBot.py file you chose.
* Finally you can just start main.py and it will start posting in your Discord channel when there are new tweets.

## Credits
Derpolino for providing the [discord-webhook-python](https://github.com/Derpolino/discord-webhooks-python) code.
Rokxx for providing the [dota 2 twitter list](https://twitter.com/rokxx/lists/dota-2/members).
JacobNWolf for providing the [twitter list](https://twitter.com/JacobNWolf/lists/) for CS:GO, LoL, Overwatch, CoD and SSMB.