---
title: "YAML Configuration"
permalink: /docs/conf-config-yaml/
excerpt: "Configuring the discord-twitter-bot through config.yml"
toc: true
---

## Location

The yaml file is located at [discord-twitter-bot/bot/config.yml](https://github.com/NNTin/discord-twitter-bot/blob/master/bot/main.yml).
By editing the config.yml file you are configuring your bot.  

## Quick Intro in how to modify any value in a .yml file

`true` and `false` are Booleans. You do not put them in "quotation marks" or 'single quotes'.  
You define a string by putting them in "quotation marks" or 'single quotes'.  
You define a list/array element by using dashes - **OR** you define a list/array element
by putting them in square brackets []. Comma separate multiple.

Be careful how you use those dashes. They are important to make your configuration work.
{: .notice--danger}

## Configuration
### Twitter

[In a previous page you've set up your Twitter App.](/discord-twitter-bot/docs/configuration/#getting-twitter-api-credentials)
Copy those keys and fill out the config.yml like this.

```
Twitter:
  access_token: 'XXX-XXX'
  access_token_secret: 'XXX'
  consumer_key: 'XXX'
  consumer_secret: 'XXX'
```

### Config.yml Example

If you are wondering what the variables are doing [read this again](http://localhost:4000/discord-twitter-bot/docs/configuration/#explanation-of-the-variables).  
In this example we provide the Twitter credentials and define 2 feeds for your text channel.  

[At the configuration page I explained how the channels in my Discord servers were configured](/discord-twitter-bot/docs/configuration/).
Here I'm showing concrete examples how they were configured in config.yml.

#### discordapp

[#discordapp](https://discordapp.com/channels/295528852518731786/557231331658956831/)

```
Discord:
  - IncludeReplyToUser: true
    IncludeRetweet: true
    IncludeUserReply: true
    twitter_ids: 3065618342
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
```

#### dota-2, lol, csgo

[#dota-2](https://discordapp.com/channels/295528852518731786/557231354316718080)  
[#lol](https://discordapp.com/channels/295528852518731786/557231372499025922)  
[#csgo](https://discordapp.com/channels/295528852518731786/557231389540352000)

```
Discord:
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists:
     - 'https://twitter.com/rokxx/lists/dota-2'
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists:
     - 'https://twitter.com/JacobWolf/lists/league-of-legends-eu'
     - 'https://twitter.com/JacobWolf/lists/league-of-legends-na'
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists: ['https://twitter.com/JacobWolf/lists/counter-strike-na1', 'https://twitter.com/JacobWolf/lists/counter-strike-eu1']
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
```

Note: I'm intentionally being inconsistent on the formatting to show the difference between using **dashes** and **square brackets**.
Do not make the mistake of defining a variable as a string if it was supposed to be a list/array of strings.

#### vietnam

[#vietnam](https://discordapp.com/channels/295528852518731786/557231418346962957)

```
Discord:
 - location: [106.405897,10.526054,106.999159,11.027906]
   webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
 - location: [105.5531,20.7885,106.1464,21.2653]
   webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
 - location: [107.372125,16.288804,107.782899,16.649613]
   webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
 - location: [108.005212,15.887674,108.415986,16.249221]
   webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
```

#### python

[#python](https://discordapp.com/channels/295528852518731786/557231451020722186)

```
Discord:
 - track:
    - 'python'
   webhook_urls:
    - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
```

#### All in One

```
Twitter:
  access_token: 'XXX-XXX'
  access_token_secret: 'XXX'
  consumer_key: 'XXX'
  consumer_secret: 'XXX'

Discord:
  - IncludeReplyToUser: true
    IncludeRetweet: true
    IncludeUserReply: true
    twitter_ids: 3065618342
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists:
     - 'https://twitter.com/rokxx/lists/dota-2'
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists:
     - 'https://twitter.com/JacobWolf/lists/league-of-legends-eu'
     - 'https://twitter.com/JacobWolf/lists/league-of-legends-na'
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: false
    twitter_lists: ['https://twitter.com/JacobWolf/lists/counter-strike-na1', 'https://twitter.com/JacobWolf/lists/counter-strike-eu1']
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
  - location: [106.405897,10.526054,106.999159,11.027906]
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - location: [105.5531,20.7885,106.1464,21.2653]
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - location: [107.372125,16.288804,107.782899,16.649613]
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - location: [108.005212,15.887674,108.415986,16.249221]
    webhook_urls: ['https://discordapp.com/api/webhooks/123456/XXXXXX']
  - track:
     - 'python'
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
```

#### An example using the other fields

```
Twitter:
  access_token: XXX-XXX
  access_token_secret: XXX
  consumer_key: XXX
  consumer_secret: XXX

Discord:
  - IncludeReplyToUser: false
    IncludeRetweet: false
    IncludeUserReply: true
    custom_message: 'A new tweet!'
    keyword_sets:
     - - 'League'    # tweet will be posted if tweet contains all 3 words {League of Legends}, no particular order.
       - 'of'
       - 'Legends'
     - - 'Dota 2'    # tweet will be posted if tweet contains 'Dota 2'. A tweet saying `2day we play Dota` will not be posted.
    blackword_sets:
     - - 'MOBA'      # tweet will not be posted if it contains 'MOBA'
    twitter_ids:
     - '123'         # define as many as you want with a dash {-} at the beginning
     - '456'
    twitter_handles:
     - 'discordapp'
    twitter_lists:
     - 'https://twitter.com/rokxx/lists/dota-2'
    track:
     - 'python'
    location: [106.405897,10.526054,106.999159,11.027906]
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXX-XXXX'
  - track:
     - 'python'
    webhook_urls:
     - 'https://discordapp.com/api/webhooks/123456/XXXXXX'
```
