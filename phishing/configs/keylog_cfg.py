import datetime
import os
import platform

WRITE_KEYLOG_OUTPATH = 'keylogs/raw_keylogs'
WRITE_KEYLOG_FILENAME =  'keylog_' + str(datetime.datetime.today()).replace(' ', '') + '.txt'


##### parse keylogged params #####

READ_KEYLOGGED_DIR = 'keylogs/raw_keylogs/'
WRITE_KEYLOGGED_DIR = 'keylogs/parsed_keylogs/'
