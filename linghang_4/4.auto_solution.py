#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re, sys

def calculate(a, operator, b):
    try:
        c = { '+': a + b, '-': a - b, '*': a * b, '/': a / b, }[operator]
        return ('{:g}'.format(c))
    except ZeroDivisionError:
        return ("除数不能为0！")
    except ValueError:
        return ("请输入正确的四则运算格式！")
q_flie = sys.argv[1]
a_file = sys.argv[2]

if not os.path.exists(q_flie):
    print('文件不存在，请输入有效文件名！')
else:
    problem = open(q_flie, 'r')
    resolve = open(a_file, 'w')

    for line in problem:
        x = re.split('(\+|-|\*|/)', line)
        resolve.write(line.strip() + '=' + str(calculate(float(x[0]), x[1], float(x[2]))) + '\n')

    problem.close()
    resolve.close()