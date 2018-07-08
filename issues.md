# Known Issues

###### Script does not post multiple pictures

This is intended. When multiple pictures are provided the script will only pick a single image. The reason behind this is [you can only attach a single image](https://cdn.discordapp.com/attachments/295595536222781451/435645322790699009/unknown.png) and a single thumbnail in a single embed. The thumbnail is not used in my script.  
I could post the picture in multiple messages or multiple embeds but it looks bad. If you want it I can point you in the right direction but I won't add it to my script.

###### Script does not post any pictures

This is outside of my control. [The tweet on Twitter has a picture](https://twitter.com/G4_LAN/status/951861333519040512). My script retrieves the data through the Twitter API. [This is what my bot sees](https://pastebin.com/tuUhiunD). The image link is not in the json. I don't know why for some tweets Twitter chooses not to include the picture hyperlink but since they are not providing it through the API I can't access it thus I can't post it to Discord.