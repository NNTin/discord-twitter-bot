---
title: "Heroku"
permalink: /docs/inst-heroku/
excerpt: "Heroku Installation and Running"
toc: true
---

TODO:
Python installation.
Pip installation.
Requirements installation.
Link configuration methods.
Running the bot.

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

<iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/NwPcXBvStSI?controls=0&showinfo=0" frameborder="0" allowfullscreen></iframe>
