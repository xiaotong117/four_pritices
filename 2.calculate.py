#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

problem = input()
x = re.split('(\+|-|\*|/)', problem)     #带括号会把分割条件也输出出来

try:
    a = float(x[0])
    b = float(x[2])
    operator = x[1]
    c = { '+': a + b, '-': a - b, '*': a * b, '/': a / b, }[operator]
    print(problem, ' = ', '{:g}'.format(c))    #结果保留6位有效数字
except ZeroDivisionError:
    print("除数不能为0！")
except :
    print("请输入正确的四则运算格式！")

