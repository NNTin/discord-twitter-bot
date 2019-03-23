var store = [{
        "title": "Documentation",
        "excerpt":"TODO: Write script that iterates over every doc in docs except itself displaying its content.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/",
        "teaser":null},{
        "title": "Installation",
        "excerpt":"Intro   This project requires Python >=3.6.0. It is untested against Python &gt;=3.7.0.   The required version-locked Python packages are listed in requirements.txt and can be installed from PyPI.org.       Install it now                                                                                                                              Ubuntu                                                    Classic Linux distribution.                                                   Read More                                                                                                                                                           Windows                                                    Everyone has a Windows machine.                                                   Read More                                                                                                                                                           Mac OS                                                    Set it up on Mac OS.                                                   Read More                                                                                                                                                                   Heroku                                                    This set up is the user-friendliest. No knowledge about command line, git, python is required!                                                   Read More                                                                                                                                                                   Docker                                                    Docker is easy to set up for power users.                                                   Read More                                                                                                                                                                   Raspbian                                                    For the tinkerers out there.                                                   Read More                                        Recommendation   Heroku has the easiest installation. However it requires a verified credit card to unlock 1000 free dyno hours per month enabling you hosting the bot 24/7. If you already have a VPS or a machine running 24/7 I recommend not using this option.   For Docker users I’ve released a Docker image which is only 31 MB big. The benefit of Docker is you can deploy it on any machine and it’ll work. Use this if you are already using Docker.   Ubuntu is the go-to OS. Some use it as their personal office OS. Often times you see this as the OS of choice for their VPS.   Everyone has a Windows machine. It’s not recommended since Windows machines usually don’t run 24/7. But if you have the money or want to try this bot out use Windows.   Mac OS: A significant amount of people are using Mac OS so I’m including this.   Honorary mention to the Raspberry Pi Community. This guide also has install introduction for Raspbian users. The Docker images are also available for the arm architecture.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/installation/",
        "teaser":null},{
        "title": "Installing the bot on Ubuntu",
        "excerpt":"   It’s recommended to install the Discord-Twitter-Bot via the command line. If you are running multiple python scripts on your server it is recommended to use virtualenv.   Installing Python3.6 and pip  Ubuntu 18.04 &amp; Ubuntu 16.04   # Install system dependencies sudo apt-get update -y sudo apt-get install git python3.6 python3.6-pip sudo apt-get upgrade -y  # Upgrading pip and installing venv sudo python3.6 -m pip install --upgrade pip   Ubuntu 14.04   # Install system dependencies sudo apt-get update -y sudo apt-get install git python3.6 sudo apt-get upgrade -y  # Install pip and installing venv curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py sudo python3.6 get-pip.py sudo python3.6 -m pip install --upgrade pip   Installing  Installing the bot with virtualenv   When running Python scripts it is recommended to use virtualenv. Without virtualenv there is a risk of breaking your Python scripts when you install other Python scripts that depend on different Python packages versions.   # Installing virtualenv python3.6 -m pip install virtualenv  # Clone the Discord-Twitter-Bot to your home directory git clone https://github.com/nntin/discord-twitter-bot.git ~/discord-twitter-bot -b master cd ~/discord-twitter-bot  # Creating the virtual environment and activating it python3.6 -m pip venv venv . venv/bin/activate  # Install Python dependencies pip install -r requirements.txt  # Exiting the virtual environment deactivate   Installing the bot without virtualenv   This is NOT recommended. The installation step without virtualenv is easier at the expense of you accidentally breaking the Python script in the future, see above for installing with virtualenv.   # Clone the Discord-Twitter-Bot to your home directory git clone https://github.com/nntin/discord-twitter-bot.git ~/discord-twitter-bot -b master cd ~/discord-twitter-bot  # Install Python dependencies pip install -r requirements.txt   Configuring the bot   Watch out! Before you can start the bot you need to configure the bot first. It needs to know which tweets it is supposed to post into your text channel.   Starting the bot   If everything was done correctly you can now start the bot.   Starting the bot with virtualenv   cd ~/discord-twitter-bot . venv/bin/activate python3.6 bot/main.py deactivate   Starting the bot without virtualenv   cd ~/discord-twitter-bot python3.6 bot/main.py   Misc   Every system is a tiny bit different. You might already had Python3.6 or you have multiple Python versions.   In this guide I wrote everywhere python3.6 to ensure you really have the correct version. It is however possible that python and python3 are using the same version as python3.6. Even if that is the case you should not use them interchangeably since it is possible you have the same version installed twice.   # Check your Python version. python -V python3 -V python3.6 -V  # Check the location of your Python version. # This is useful if you want to run your script in systemd which python3.6  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-ubuntu/",
        "teaser":null},{
        "title": "Windows",
        "excerpt":"TODO: Python installation. Pip installation. Requirements installation. Link configuration methods. Running the bot.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-windows/",
        "teaser":null},{
        "title": "MacOS",
        "excerpt":"TODO: Python installation. Pip installation. Requirements installation. Link configuration methods. Running the bot.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-macos/",
        "teaser":null},{
        "title": "Heroku",
        "excerpt":"TODO: Python installation. Pip installation. Requirements installation. Link configuration methods. Running the bot.   Heroku Deployment      Remember to activate the app. View the logs here.  Use this to initially deploy your discord-twitter-bot.   To further configure the bot get Heroku CLI and run launcher.py. (Warning: This is not recommended for inexperienced users since a lot of things could go wrong.)   heroku login heroku create &lt;your heroku app name&gt; cd &lt;your heroku app name&gt; git remote add origin https://github.com/NNTin/discord-twitter-bot git pull origin master python bot/launcher.py git add . git commit -am \"updated configuration\" git push heroku   This will create a data.json and the bot will ignore any set environment variable.   YT Video to Heroku Deployment    ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-heroku/",
        "teaser":null},{
        "title": "Docker",
        "excerpt":"TODO: Python installation. Pip installation. Requirements installation. Link configuration methods. Running the bot.   Docker Setup  (Warning: This is only recommended for experienced users who have some basic experience with Docker.)   nano .env docker run --env-file ./.env nntin/discord-twitter-bot   .env file example  ACCESS_TOKEN=XXX-XXX ACCESS_TOKEN_SECRET=XXX CONSUMER_KEY=XXX CONSUMER_SECRET=XXX TWITTER_ID=123,456,789 TWITTER_LIST=https://twitter.com/rokxx/lists/dota-2 TWITTER_HANDLE=discordapp WEBHOOK_URL=https://discordapp.com/api/webhooks/123456789/XXXX-XXXX   Optional environment variables: INCLUDE_REPLY_TO_USER, INCLUDE_RETWEET, INCLUDE_USER_REPLY, CUSTOM_MESSAGE, KEYWORDS   One of the 3 environment variables are required: TWITTER_ID, TWITTER_LIST and TWITTER_HANDLE. You can specify all three.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-docker/",
        "teaser":null},{
        "title": "Raspbian",
        "excerpt":"TODO: Python installation. Pip installation. Requirements installation. Link configuration methods. Running the bot.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/inst-raspbian/",
        "teaser":null},{
        "title": "Configuration",
        "excerpt":"TODO: Write small description about the configuration methods.  Maybe remove this page -&gt; unnecessary.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/configuration/",
        "teaser":null},{
        "title": "YAML Configuration",
        "excerpt":"TODO: Write a quick start config.yml tutorial. Then go in depth explaining twitter id, twitter list, location, track, filtering, keywords, … .  Finally show a config.yml as it is used in Discord server.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/conf-config-yaml/",
        "teaser":null},{
        "title": "Environment Variable",
        "excerpt":"TODO: Write a quick start .env tutorial. Then go in depth explaining twitter id, twitter list, location, track, filtering, keywords, … .  Finally show a .env as it is used in Discord server.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/conf-environment-variable/",
        "teaser":null},{
        "title": "Extra",
        "excerpt":"TODO: Maybe remove this page -&gt; unnecessary.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/extra/",
        "teaser":null},{
        "title": "Extra",
        "excerpt":"TODO: Write some potential Questions with Answers.   Why?  Q: Why Heroku?  A: Heroku has a lot of bad reputation for being an inferior hosting service. The heroku dynos restart roughly every 24 hours and data are lost. However Heroku can be incredibly user friendly once it is properly set up. No knowledge about git, ssh and python is required. I personally don’t host anything on Heroku but I appreciate Heroku since it is a free hosting solution and it can be very user friendly (but not developer friendly).   Q: Why add automated testing and automated docker image deployment for a relatively simple solo project? Isn’t this overkill?  A: Continuous integration/deployment is incredible useful in bigger projects. It cuts down development time. I contributed to other FOSS projects that had CI/CD and I was interested how the flow was actually implemented.   Q: Why Travis and Azure Pipelines?  I added Travis CI support first. But then I learned about how they were acquired by another company and there was a massive layoff. I then looked for alternatives in case the Travis becomes less user friendly and Azure Pipelines seemed like a good choice. I have migrated from Travis to Azure Pipelines but I will keep both around for educational purposes.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/faq/",
        "teaser":null},{
        "title": "Troubleshooting",
        "excerpt":"TODO: Provide some test for troubleshooting (running tox).  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/troubleshooting/",
        "teaser":null},{
        "title": "Known Issues",
        "excerpt":"Script does not post multiple pictures   This is intended. When multiple pictures are provided the script will only pick a single image. The reason behind this is you can only attach a single image and a single thumbnail in a single embed. The thumbnail is not used in my script.  I could post the picture in multiple messages or multiple embeds but it looks bad. If you want it I can point you in the right direction but I won’t add it to my script.   Script does not post any pictures   This is outside of my control. The tweet on Twitter has a picture. My script retrieves the data through the Twitter API. This is what my bot sees. The image link is not in the json. I don’t know why for some tweets Twitter chooses not to include the picture hyperlink but since they are not providing it through the API I can’t access it thus I can’t post it to Discord.   I can’t get my Twitter application approved   That’s a tough one I cannot easily answer.    There was one guy who had a Twitter account since 2009 and it took him 3 weeks to get his app approved.    Meanwhile when he created a new account and applied for it it got accepted right away. Another guy had his app approved after he confirmed his e-mail.   So my advice is to confirm e-mail and if that doesn’t work create a (throwaway) Twitter account with confirmed e-mail and try again.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/issues/",
        "teaser":null},{
        "title": "Resources & Credits",
        "excerpt":"Credits  Rokxx for providing the dota 2 twitter list.  JacobWolf for providing the twitter lists for CS:GO, LoL, Overwatch, CoD and SSMB.   Useful links     Twitter API   What’s a webhook?  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/discord-twitter-bot/docs/resources/",
        "teaser":null},]
