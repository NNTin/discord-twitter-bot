---
title: "Heroku"
permalink: /docs/inst-heroku/
excerpt: "Heroku Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/heroku.png" alt="Heroku" style="width: 150px; float: right;"/>
This is by far the easiest installation method.

## Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FNNTin%2Fdiscord-twitter-bot&template=https%3A%2F%2Fgithub.com%2FNNTin%2Fdiscord-twitter-bot)

Remember to [activate](https://i.imgur.com/zOfa0Qm.png) the app. [View the logs here.](https://i.imgur.com/tWBoTuB.png)  
Use this to initially deploy your discord-twitter-bot.

## YT Video to Heroku Deployment
<iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/NwPcXBvStSI?controls=0&showinfo=0" frameborder="0" allowfullscreen></iframe>

## Further Configuration
You can go into the settings tab and edit the environment variables there.
Head over to [Configuration](/discord-twitter-bot/docs/configuration #) to
see how environment variables work.  
After editing the configuration you have to deactivate and activate the app.

## Misc
The ease of usage has a cost. First you need a verified credit card in order
to host the bot 24/7. Although this doesn't cost anything a lot of people
don't have access to a credit card.  
Furthermore Heroku Dynos restart every 24 hours so it is possible it might
be missing some tweets during the startup time.
