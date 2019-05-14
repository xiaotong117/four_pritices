#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

a =['333', '222']
q= ''
for x in a:
    q+=x+'\n'
s = '111\n'+q+'444'
print(s)