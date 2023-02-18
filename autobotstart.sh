#! /bin/bash


# See more info about this shell script:
# https://github.com/hms5232/get-LAN-IP-telegram-bot


# Change path depend on your env
cd /home/pi/Documents/get-LAN-IP-telegram-bot

# =======================
# Please choose one way
# depend on how you 
# install python package
# 
# and
# 
# don't forget edit
# 	/etc/rc.local
# run this script
# when start
# =======================

# Use Poetry
# Change Poetry binary path depend on your env
# Change log path if you need (or remove output log command)
/home/pi/.local/bin/poetry run python3 bot.py > /home/pi/Documents/get-LAN-IP-telegram-bot/autorunbot.log 2>&1 &

# or

# General (install package directly on system)
# Change log path if you need (or remove output log command)
#python3 bot.py > /home/pi/Documents/get-LAN-IP-telegram-bot/autorunbot.log 2>&1 &
