#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('这是个debug级别的信息')#输出时被过滤掉了
logging.info('这是个info级别的信息')#输出时被过滤掉了
logging.warning('这是个warning级别的信息')
logging.error('这是个error级别的信息')
logging.critical('这是个critical级别的信息')

order = '13231'
c = [40]
a = [20]
if c[0] == a[0]*2 :
    print('111')


if 6 in [4,5,6]:
    print('213')