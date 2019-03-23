---
title: "Extra"
permalink: /docs/faq/
excerpt: "Frequently Asked Questions, nowadays known as Questions and Answers"
toc: true
---

TODO:
Write some potential Questions with Answers.

##  Why?
Q: Why Heroku?  
A: Heroku has a lot of bad reputation for being an inferior hosting service. The heroku dynos restart roughly every 24 hours and data are lost. However Heroku can be incredibly user friendly once it is properly set up. No knowledge about git, ssh and python is required. I personally don't host anything on Heroku but I appreciate Heroku since it is a free hosting solution and it can be very user friendly (but not developer friendly).

Q: Why add automated testing and automated docker image deployment for a relatively simple solo project? Isn't this overkill?  
A: Continuous integration/deployment is incredible useful in bigger projects. It cuts down development time. I contributed to other FOSS projects that had CI/CD and I was interested how the flow was actually implemented.

Q: Why Travis and Azure Pipelines?  
I added Travis CI support first. [But then I learned about how they were acquired by another company and there was a massive layoff.](https://twitter.com/carmatrocity/status/1098538649908666368) I then looked for alternatives in case the Travis becomes less user friendly and Azure Pipelines seemed like a good choice. I have migrated from Travis to Azure Pipelines but I will keep both around for educational purposes.
