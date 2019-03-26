---
title: "systemd"
permalink: /docs/systemd/
excerpt: "Set it up as a service with systemd"
toc: true
---

## Intro

Are you wondering how you can keep the bot running after closing the terminal? This page
addresses that problem.  

You may be already familiar with tmux or screen. And although those allow you to keep
your program running they face 2 major problems:  
After your VPS restarts your script is no longer running. Furthermore if your script runs
into an error, e.g. it lost internet connection, it will stop functioning.  

Systemd solves it. It runs in the background, starts up the service even after a server
restart and when an error happens you can set it to rerun the script.

This guide is written for Linux users!

## Main Body

This part hasn't been written yet. In the mean time please do your own research. Systemd
is widely used so you will find a lot of resources. Developers make use of it very
extensively.
