#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re

def calculate(a, operator, b):
    try:
        c = { '+': a + b, '-': a - b, '*': a * b, '/': a / b, }[operator]
        return (c)
    except ZeroDivisionError:
        return ("除数不能为0！")
    except ValueError:
        return ("请输入正确的整数四则运算格式！")

a = input().split()
if not os.path.exists(a[0]):
    print('文件不存在，请输入有效文件名！')
else:
    problem = open(a[0], 'r')
    resolve = open(a[1], 'w')

    for line in problem:
        x = re.split('\D', line)
        operator = re.search('\D', line).group()
        resolve.write(line.strip() + '=' + str(calculate(int(x[0]), operator, int(x[1]))) + '\n')

    problem.close()
    resolve.close()