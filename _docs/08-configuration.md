---
title: "Configuration"
permalink: /docs/configuration/
excerpt: "Configuring the discord-twitter-bot"
feature_row1:
  - image_path: /assets/images/yaml.png
    alt: "YAML"
    title: "YAML"
    excerpt: 'Configure the bot through YAML. This is easy to read but you need to follow the syntax closely!'
    url: "/docs/conf-config-yaml/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row2:
  - image_path: /assets/images/dotenv.png
    alt: "Docker"
    title: "Docker"
    excerpt: "Not recommended but in some cases you don't have any other option."
    url: "/docs/conf-environment-variable/"
    btn_label: "Read More"
    btn_class: "btn--primary"
toc: true
---

## Intro

There are 2 methods to configure the bot: Editing config.yml or using
environment variables.

{% include feature_row id="feature_row1" type="left" %}

{% include feature_row id="feature_row2" type="right" %}

If at any point you run into a problem please check out [troubleshooting](/discord-twitter-bot/docs/troubleshooting/) first.  
I've poured a lot of time into writing this guide and it feels bad if people ask questions
that has been already answered in this guide.  
If you've read something in this guide and did not understand it please feel free to reach out to me.

## Recommendation

The recommended configuration method is by editing
the config.yml file. However that option is not always available so you could
use the default config.yml file and fill it with environment variables. E.g.
when deploying the bot via Heroku.  
In all the other scenarios you can edit config.yml.


## Getting Twitter API Credentials

TODO.

## Explanation of the variables

With the exception of the `webhook_urls` none of the other variables are mandatory.  
You could just define a webhook url and a twitter id and it will post just fine. Or a
webhook url and a location box.

### IncludeReplyToUser

If you are tracking a twitter user through `twitter_ids`, `twitter_lists` or `twitter_handles`
this variable determines if tweets **from random twitter user to your followed twitter user**
should be displayed or not.

### IncludeUserReply

If you are tracking a twitter user through `twitter_ids`, `twitter_lists` or `twitter_handles`
this variable determines if tweets **from your followed twitter user to random twitter user**
should be displayed or not.

### IncludeRetweet

This variable determines whether a retweet should be displayed or not.

### custom_message

If you want to supply a custom message you can do it here. This could be used to ping
certain roles or users.  
Ping yourself on Discord and put the escape letter in front of the mention.  
If you for example send `I'm pinging \@Linley#8686` in chat you will see  
`I'm pinging <@77488778255540224>`.  
This is the syntax you are going to need to provide in `custom_message` if you
want to ping a user. You can try it with roles as well.

### keyword_sets

The tweet will be only be posted when certain keywords are present. You can make it
only post when a combination of keywords are present or if a single out of many keywords are present.  

You can imagine it if any **set** of the keyword sets are present it will be posted. A
set can contain a single keyword but it could also contain multiple keywords.

### blackword_sets

Same as `keyword_sets` but the opposite scenario. Don't post the tweet when a blackword
set is present.

### twitter_ids

This is the recommended way of following certain Twitter users. A twitter handle can
change so it's not reliable. Twitter lists may change unbeknownst to you. You can get
the twitter id from [here](http://gettwitterid.com/).  

Furthermore when you define `twitter_handles` or `twitter_lists` they will be converted
to `twitter_ids` which can take a while. To minimize the script boot time you should
try configure it through twitter_ids.

### twitter_handles

A more user friendly way of defining the value. The twitter handle is part of the link
when you visit a Twitter Profile. When you ping a Twitter user you do `@twitter_handle`.
Don't confuse it with someone's Twitter name which can be different from the Twitter
handle.

### twitter_lists

If you are maintaining or know someone who is maintaining a Twitter list you could use that.  

Here is an example how it could look like:  
https://twitter.com/rokxx/lists/dota-2


### track

If you want to get tweets beyond from certain users you can use this. But beware if you
use a really common word you will get a lot of tweets which will lead to being rate limited
by Discord.  
You can make it only retrieve hashtags by prefixing it with a hashtag #.

### location

If you want to get location based tweets you can define a location box. [Use this website](http://boundingbox.klokantech.com/).  
Beware. Don't use a location box that is too big. You will be rate limited by Discord.  
Bear in mind that not everyone reveals their geolocation.

### webhook_urls

This is what enables the bot to post in your text channel. [Discord has written a nice article about it.](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Discord Server Example

In order for the following links to work you have to be part of my Discord Server. [Join here](https://discord.gg/Dkg79tc)  
It is explained in the next pages how the config.yml or .env file have to look like to reproduce
those twitter feeds.

### discordapp

[#discordapp](https://discordapp.com/channels/295528852518731786/557231331658956831/)

Set to follow [@discordapp](https://twitter.com/discordapp). `IncludeRetweet`, `IncludeUserReply`, `IncludeReplyToUser` is set
to `True`. This was configured through the variable `twitter_ids`

### dota-2, lol, csgo

[#dota-2](https://discordapp.com/channels/295528852518731786/557231354316718080)  
[#lol](https://discordapp.com/channels/295528852518731786/557231372499025922)  
[#csgo](https://discordapp.com/channels/295528852518731786/557231389540352000)

`IncludeRetweet`, `IncludeUserReply`, `IncludeReplyToUser` is set to `False`.  
This was configured through `twitter_lists`. The twitter list URLs can be found [here](/discord-twitter-bot/docs/resources/).

### vietnam

[#vietnam](https://discordapp.com/channels/295528852518731786/557231418346962957)

I've defined 4 webhooks for this channel. Each webhook represents a city in Vietnam. Those are
the cities Saigon, Da Nang, Hue and Hanoi.  

For each webhook I provided a location box.

### python

[#python](https://discordapp.com/channels/295528852518731786/557231451020722186)

This channel posts any tweet that says `python` on Twitter. If I would have written
`#python` it would explicitly only look for the hashtag. I chose not to since the tweets
that were posted were very infrequent.
