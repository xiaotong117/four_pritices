#!/usr/bin/python

import re

problem = input()

x = re.split('\D', problem, re.M | re.I)
operator = re.search('\D', problem, re.M | re.I).group()

try:
    a = int(x[0])
    b = int(x[1])
    c = { '+': a + b, '-': a - b, '*': a * b, '/': a / b, }[operator]
    print(problem + ' = ' + str(c))
except ZeroDivisionError:
    print("除数不能为0！")
except ValueError:
    print("请输入正确的四则运算格式！")

