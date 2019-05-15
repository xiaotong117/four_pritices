#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

a={'apple':1, 'bpple':1,'cpple':1,'dpple':2,'epple':1,'fpple':1}
b={'apple':1, 'bpple':1,'cpple':1,'dpple':1,'epple':1,'gpple':1,'hpple':1}
for k in list(a.keys()):
    if k in b:
        if a[k] == b[k]:
            print(k, '相同')
            del a[k]
            del b[k]
        else:
            print(k, '不同')
            del a[k]
            del b[k]
    else:
        print(k, '不同')
if b:
    for k in b.keys():
        print(k, '不同')

print('a:')
print(a)
print('b:')
print(b)

