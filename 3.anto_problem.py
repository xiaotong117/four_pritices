#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

a = input().split()
num = int(a[0])
file = a[1]

fo = open(file, 'w')
for x in range(num):
    fo.write(str(random.randint(0, 99)) + random.choice('+-*/') + str(random.randint(1, 99)) + '\n')
fo.close()
