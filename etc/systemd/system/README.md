# Prologue

Systemd is a nice tool to start, stop and restart scripts on your linu machine. If your script crashes or the VPS does a system reboot your scripts will come back online.  
In order to use this you need to be on Linux, have systemd, the discord-twitter-bot has been properly installed and it has worked before.

# Setup

Copy the dtb.service file and put it to /etc/systemd/system  
`cp dtb.service /etc/systemd/system/dtb.service`

Edit dtb.service  
`nano /etc/systemd/system/dtb.service`

Adjust the `WorkingDirectory` to the path you git cloned the `discord-twitter-bot` folder/repository.  

Adjust the path of your python executable (first parameter of `ExecStart`):   
```coffeescript
tin@Riftshadow:~# which python3
/usr/bin/python3
tin@Riftshadow:~# which python3.5
/usr/bin/python3.5
```

Adjust the path to main.py (second parameter of `ExecStart`)     
`<...>/discord-twitter-bot/bot/main.py`

# systemd commands

```coffeescript
sudo systemctl start dtb.service
sudo systemctl enable dtb.service
sudo systemctl disable dtb.service
sudo systemctl stop dtb.service
sudo systemctl restart dtb.service
```

`enable` means that the service is automatically started when your VPS boots up.