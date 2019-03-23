---
title: "FAQ"
permalink: /docs/faq/
excerpt: "Frequently Asked Questions also known as potential Questions and Answers"
toc: true
---

Frequently Asked Questions also known as potential Questions and Answers

# Q: Why Heroku?  
A: Heroku has a lot of bad reputation for being an inferior hosting service. The heroku dynos restart roughly every 24 hours and data are lost. However Heroku can be incredibly user friendly once it is properly set up. No knowledge about git, ssh and python is required. I personally prefer using a VPS but I appreciate Heroku since it is a free hosting solution and it can be very user friendly (but not developer friendly). There are a lot of developers that look down on Heroku but simultaneously most of my users are using Heroku to deploy their bot.

# Q: Why add automated testing, automated docker image deployment and Jekyll GitHub Pages for a relatively simple solo project? Isn't this overkill?  
A: Continuous integration/deployment is incredible useful in bigger projects. It cuts down development time. I contributed to other FOSS projects that had CI/CD and I was interested how the flow was actually implemented. Same story with Jekyll. (My second website project after [discord-logo](https://nntin.github.io/discord-logo))

# Q: Why Travis and Azure Pipelines?  
I added Travis CI support first. [But then I learned about how they were acquired by another company and there was a massive layoff.](https://twitter.com/carmatrocity/status/1098538649908666368) To futureproof myself I looked for alternatives in case Travis becomes less user friendly and Azure Pipelines seemed like a good choice. I have migrated from Travis to Azure Pipelines but I will keep both around for educational purposes.

# Q: How can I support you?
The best way of supporting me is just using the project. I like giving back to the community and what is especially satisfying is to have your work recognized as simple as it may be.
