#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys, re, datetime

'''控制台运行 date.py 2019-01-05 ,控制台输出2019年是平年，01月05日是一年中的第5天'''

# s = re.split('-', sys.argv[1])
# year, month, day = s[0], s[2], s[4]
a = datetime.date.strftime(sys.argv[1],'%Y-%m-%d')
print(a.timetuple().tm_yday)

# if s % 4 == 0:
#     print(year, '是闰年，')
