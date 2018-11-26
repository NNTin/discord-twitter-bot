# Issues

#### Script does not post multiple pictures

This is intended. When multiple pictures are provided the script will only pick a single image. The reason behind this is [you can only attach a single image](https://cdn.discordapp.com/attachments/295595536222781451/435645322790699009/unknown.png) and a single thumbnail in a single embed. The thumbnail is not used in my script.  
I could post the picture in multiple messages or multiple embeds but it looks bad. If you want it I can point you in the right direction but I won't add it to my script.

#### Script does not post any pictures

This is outside of my control. [The tweet on Twitter has a picture](https://twitter.com/G4_LAN/status/951861333519040512). My script retrieves the data through the Twitter API. [This is what my bot sees](https://pastebin.com/tuUhiunD). The image link is not in the json. I don't know why for some tweets Twitter chooses not to include the picture hyperlink but since they are not providing it through the API I can't access it thus I can't post it to Discord.

#### I can't get my Twitter application approved

That's a tough one I cannot easily answer.    
There was one guy who had a Twitter account since 2009 and it took him 3 weeks to get his app approved.    
Meanwhile when he created a new account and applied for it it got accepted right away. Another guy had his app approved after he confirmed his e-mail.

So my advice is to confirm e-mail and if that doesn't work create a (throwaway) Twitter account with confirmed e-mail and try again.

#### Configuration with Heroku is limited

I offer Heroku support because it is easy to use. With a [few clicks](https://www.youtube.com/watch?v=NwPcXBvStSI) you have your bot up and running for free. If you want to follow more twitter users or maintain multiple twitter id lists each posting to a different text channel and so on you will have to manually set it up.

This is **not** a user friendly process and can be overwhelming for a novice. The degree of difficulty is similar to hosting it on a VPS.

The very reason I offer Heroku support is because it eliminates a lot of user created errors. It's a nightmare for me to troubleshoot the errors. For instance people already have Python installed and rely on libraries with different versions (use venv...). They have Python installed but do not know how to call it or they are calling Python but unbeknown to them they are using a different version or they haven't added Python to PATH or they are opening Python by opening python.exe instead of calling it from CLI...  
This is why I won't offer more support than this. There is also git, Heroku CLI. People often get stuck because they are too many things they need to be aware of. Forgetting a single step means the program won't run. And the steps may look different from system to system.

See [README.md](https://github.com/NNTin/discord-twitter-bot) on how to host the bot with Heroku and using launcher.py. This will create a data.json and any environment variables set in Heroku will be ignored.  
Further assistance will not be given.
