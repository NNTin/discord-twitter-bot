---
title: "Docker"
permalink: /docs/inst-docker/
excerpt: "Docker Installation and Running"
toc: true
---

<img class="doc-img" src="{{ site.baseurl }}/assets/images/docker.png" alt="Docker" style="width: 150px; float: right;"/>
With Docker you don't have to worry about installing dependencies. It's
already installed in form of an image. You just execute the image and get
a Docker container.

The requirement of this is you have Docker installed. Since installation steps
vary a lot from system to system I won't provide a guide at this moment.

## Docker images

[Docker images are available on Docker Hub.](https://cloud.docker.com/repository/docker/nntin/discord-twitter-bot/tags)
The image is available as a multi-architecture image. This means it works
on an arm architecture (e.g. Raspberry Pi) as well!

There are 3 maintained tags:  
* latest: stable release
* dev: early release, should be stable
* azure: work in progress, may be broken

If you do not specify a tag you are automatically using latest.
{: .notice--success}

## Configuring the bot

[Configure the bot first](/discord-twitter-bot/docs/configuration #). It needs
to know which tweets it is supposed to post into your text channel.

## Running the bot

Depending on which configuration method you picked you have 2 options. Running
the image by supplying an .env file or by mounting your custom
[config.yml](https://github.com/NNTin/discord-twitter-bot/blob/azure/bot/config.yml)

### .env file

```
docker run --env-file ./.env nntin/discord-twitter-bot
```

### mounting config.yml

```bash
docker run -v config.yml:/app/bot/config.yml:ro
```

## Misc

Out of all the installation methods this is by far my most favorite one.
However I do know Docker is not for everyone. This is recommended for people
who are already into Docker and maybe if you are struggling with the other
installation guides.
