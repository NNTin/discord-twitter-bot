---
title: "Installing the bot on Ubuntu"
permalink: /docs/inst-ubuntu/
excerpt: "Ubuntu Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/ubuntu.png" alt="Ubuntu" style="width: 100px; float: right;"/>

It's recommended to install the Discord-Twitter-Bot via the command line.
If you are running multiple python scripts on your server it is recommended
to use [virtualenv](#installing-the-bot-with-virtualenv).

## Installing Python3.6 and pip
### Ubuntu 18.04 & Ubuntu 16.04

```bash
# Install system dependencies
sudo apt-get update -y
sudo apt-get install git python3.6 python3.6-pip
sudo apt-get upgrade -y

# Upgrading pip and installing venv
sudo python3.6 -m pip install --upgrade pip
```

### Ubuntu 14.04

```bash
# Install system dependencies
sudo apt-get update -y
sudo apt-get install git python3.6
sudo apt-get upgrade -y

# Install pip and installing venv
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.6 get-pip.py
sudo python3.6 -m pip install --upgrade pip
```


## Installing
When running Python scripts it is [recommended](#installing-the-bot-with-virtualenv)
to use virtualenv. Without virtualenv there is a risk of breaking your Python
scripts when you install other Python scripts that depend on different Python
packages versions.
{: .notice--success}

### Installing the bot with virtualenv
```bash
# Installing virtualenv
python3.6 -m pip install virtualenv

# Clone the Discord-Twitter-Bot to your home directory
git clone https://github.com/nntin/discord-twitter-bot.git ~/discord-twitter-bot -b master
cd ~/discord-twitter-bot

# Creating the virtual environment and activating it
python3.6 -m pip venv venv
. venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Exiting the virtual environment
deactivate
```


### Installing the bot without virtualenv

```bash
# Clone the Discord-Twitter-Bot to your home directory
git clone https://github.com/nntin/discord-twitter-bot.git ~/discord-twitter-bot -b master
cd ~/discord-twitter-bot

# Install Python dependencies
python3.6 -m pip install -r requirements.txt
```

`python3.6 -m` is necessary. Else it is possible you are installing the
dependencies on another Python version!
{: .notice--warning}

## Configuring the bot

**Watch out!** Before you can start the bot you need to
[configure the bot first](/discord-twitter-bot/docs/configuration #). It needs
to know which tweets it is supposed to post into your text channel.
{: .notice--danger}

## Starting the bot

If everything was done correctly you can now start the bot.
{: .notice--success}

### Starting the bot with virtualenv

```bash
cd ~/discord-twitter-bot
. venv/bin/activate
python3.6 bot/main.py
deactivate
```

### Starting the bot without virtualenv

```bash
cd ~/discord-twitter-bot
python3.6 bot/main.py
```

## Misc

Every system is a tiny bit different. You might already had Python3.6 or you
have multiple Python versions.

In this guide I wrote everywhere `python3.6` to ensure you really have the
correct version. It is however possible that `python` and `python3` are using
the same version as `python3.6`. Even if that is the case you should not use
them interchangeably since it is possible you have the same version installed
twice.  


```bash
# Check your Python version.
python -V
python3 -V
python3.6 -V

# Check the location of your Python version.
# This is useful if you want to run your script in systemd
which python3.6
```
