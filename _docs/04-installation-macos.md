---
title: "MacOS"
permalink: /docs/inst-macos/
excerpt: "Mac OS Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/macos.png" alt="MacOS" style="width: 120px; float: right;"/>
Since I do not have a Mac I cannot tell if these install instructions work.
I am relying on your feedback to keep this page up to date.

## Installation

```bash
# Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
xcode-select --install

# Install dependencies
brew install git
brew unlink python
brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb

# Clone the Discord Twitter Bot
cd desktop
git clone https://github.com/nntin/discord-twitter-bot.git discord-twitter-bot -b master

# Install Python dependencies
cd discord-twitter-bot
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Configuring the bot

**Watch out!** Before you can start the bot you need to
[configure the bot first](/discord-twitter-bot/docs/configuration). It needs
to know which tweets it is supposed to post into your text channel.
{: .notice--danger}

## Running the bot

Open the command prompt, navigate to the folder and write
```bash
cd desktop/discord-twitter-bot
python3 bot/main.py
```
