---
title: "Windows"
permalink: /docs/inst-windows/
excerpt: "Windows Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/windows.png" alt="Windows" style="width: 100px; float: right;"/>

Discord-Twitter-Bot runs on all versions of Windows.

## Install Python

This project requires Python >=3.6.0. If you don't have Python or you have
the wrong version download Python [here](https://www.python.org/downloads/).  

You can check the version of your python in your command prompt with
`python -V`.  

During the setup it is important that you tick **Add Python 3.6 to PATH**.  

Go into the command prompt again and check if the Python version is accessible
there with `python -V`.  
Windows is finnicky. Instead of `python` your variable may be called `py`,
`py3` or `python3`.  

In this documentation I will use `py -3.6` instead of `python`, `python3`,
`py` and `py3`. This is an acceptable syntax that should always work.  
{: .notice--warning}

Do not use `py -3.6`, `python`, `python3`, `py` and `py3` interchangeably.
Stick to one else things can break.
{: .notice--danger}

## Downloading the Discord-Twitter-Bot

You have two options here. Either through `git` or by downloading the `zip`
and unpacking it e.g. with WinRAR.

Git method:
```bash
git clone https://github.com/NNTin/discord-twitter-bot.git
```

Zip method:
[Click to download](https://github.com/NNTin/discord-twitter-bot/archive/master.zip), then unpack it.

## Configuring the bot

**Watch out!** Before you can start the bot you need to
[configure the bot first](/discord-twitter-bot/docs/configuration). It needs
to know which tweets it is supposed to post into your text channel.
{: .notice--danger}

## Installing dependencies and starting the bot

Open the command prompt, navigate to the folder and write
```bash
py -36 -m pip install -r requirements.txt
py -36 bot/main.py
```

## Misc

There is a reason why hardly most programs are run on Linux servers. The setup
is more complicated and it consumes more computational resources and energy.

If this is too hard for you I recommend reading through the other installation
methods and doing them instead.
