---
title: "Resources & Credits"
permalink: /docs/resources/
excerpt: "Used Resources and Credits"
toc: false
links:
  - label: "Rokxx"
    icon: "fab fa-fw fa-twitter-square"
    url: "https://twitter.com/rokxx/lists"
  - label: "JacobWolf"
    icon: "fab fa-fw fa-twitter-square"
    url: "https://twitter.com/JacobWolf/lists"
---

## Useful links
* [Twitter API](https://developer.twitter.com/en/apps)
* [What's a webhook?](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
* [Discord.py](https://discordpy.readthedocs.io/en/rewrite/api.html#webhook-support)
* [Docker](https://docs.docker.com/engine/reference/run/)
* [Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/)
* [Heroku](https://devcenter.heroku.com/articles/heroku-button)
* [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)

# Credits
I would like to thank especially.

## Twitter Lists
{% for link in page.links %}
<a href="{{ link.url }}" rel="nofollow noopener noreferrer"><i class="{{ link.icon | default: 'fas fa-link' }}" aria-hidden="true"></i> {{ link.label }}</a>
{% endfor %}

## This website
<a href="https://jekyllrb.com" rel="nofollow">Jekyll</a> &amp; <a href="https://mademistakes.com/work/minimal-mistakes-jekyll-theme/" rel="nofollow">Minimal Mistakes</a>.
