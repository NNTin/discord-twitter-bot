#!/bin/bash

repository="https://github.com/NNTin/discord-twitter-bot.git"
localFolder="/home/pi/Desktop/discord-twitter-bot"
sensitive="/home/pi/Desktop/sensitive/discord-twitter-bot"

cd "$localFolder"

git pull "$repository"

cp "$sensitive/data.json" "$localFolder/data.json"

until python3 main.py; do
    echo "Respawning.." >&2
    sleep 1
done