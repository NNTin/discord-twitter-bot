---
title: "Installation"
permalink: /docs/installation/
excerpt: "Installation Quick Start"
feature_row:
  - image_path: assets/images/ubuntu.png
    alt: "Ubuntu"
    title: "Ubuntu"
    excerpt: "Classic Linux distribution."
    url: "/docs/inst-ubuntu/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: /assets/images/windows.png
    alt: "Windows"
    title: "Windows"
    excerpt: "Everyone has a Windows machine."
    url: "/docs/inst-windows/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: /assets/images/macos.png
    alt: "Mac OS"
    title: "Mac OS"
    excerpt: "Set it up on Mac OS."
    url: "/docs/inst-macos/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row2:
  - image_path: /assets/images/heroku.png
    alt: "Heroku"
    title: "Heroku"
    excerpt: 'This set up is the user-friendliest. No knowledge about command line, git, python is required!'
    url: "/docs/inst-heroku/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row3:
  - image_path: /assets/images/docker.png
    alt: "Docker"
    title: "Docker"
    excerpt: 'Docker is easy to set up for power users.'
    url: "/docs/inst-docker/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row4:
  - image_path: /assets/images/raspbian.png
    alt: "Raspbian"
    title: "Raspbian"
    excerpt: 'For the tinkerers out there.'
    url: "/docs/inst-raspbian/"
    btn_label: "Read More"
    btn_class: "btn--primary"
toc: true
---

## Intro

This project requires Python >=3.6.0. It is untested against Python >=3.7.0.

*[>=3.6.0]: Python 3.6.0 and greater: 3.6.0, 3.6.1, 3.6.2, 3.6.3, ...*

The required version-locked Python packages are listed in
[requirements.txt](https://github.com/NNTin/discord-twitter-bot/blob/master/requirements.txt)
and can be installed from [PyPI.org](https://pypi.org/).

<br>

## Install it now

{% include feature_row %}

{% include feature_row id="feature_row2" type="left" %}

{% include feature_row id="feature_row3" type="right" %}

{% include feature_row id="feature_row4" type="left" %}

## Recommendation

Heroku has the easiest installation. However it requires a verified credit
card to unlock 1000 free dyno hours per month enabling you hosting the bot
24/7. If you already have a VPS or a machine running 24/7 I recommend not
using this option.

For Docker users I've released a Docker image which is only 31 MB big. The
benefit of Docker is you can deploy it on any machine and it'll work. Use
this if you are already using Docker.

Ubuntu is the go-to OS. Some use it as their personal office OS. Often times
you see this as the OS of choice for their VPS.

*[VPS]: Virtual Private Server*

Everyone has a Windows machine. It's not recommended since Windows machines
usually don't run 24/7. But if you have the money or want to try this bot
out use Windows.

Mac OS: A significant amount of people are using Mac OS so I'm including this.

Honorary mention to the Raspberry Pi Community. This guide also has install
introduction for Raspbian users. The Docker images are also available for
the arm architecture.
