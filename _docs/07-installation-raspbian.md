---
title: "Raspbian"
permalink: /docs/inst-raspbian/
excerpt: "Raspbian Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/raspbian.png" alt="Raspbian" style="width: 150px; float: right;"/>
Although I no longer use Raspberry Pi for hosting scripts I first started out
hosting my scripts on a Raspberry Pi.

## Installing Python3.6

```bash
# Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install dependencies
sudo apt install python3.6
sudo apt install python3.6-pip
sudo apt install git
```

## Installing the bot

```bash
cd ~
git clone https://github.com/nntin/discord-twitter-bot.git discord-twitter-bot -b master
cd discord-twitter-bot
sudo python3.6 -m pip install --upgrade pip
sudo python3.6 -m pip install -r requirements.txt
```

## Configuring the bot

**Watch out!** Before you can start the bot you need to
[configure the bot first](/discord-twitter-bot/docs/configuration). It needs
to know which tweets it is supposed to post into your text channel.
{: .notice--danger}

## Starting the bot

After you have set it all up you can run the script with:
```bash
cd ~/discord-twitter-bot
python3.6 bot/main.py
```

## Misc

If you have a stable internet connection and you are using your RPi e.g.
for some home automation why not run this script on it?  
It will have barely any effect on the CPU load since it is mostly just
doing API calls.  
