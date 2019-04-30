#!/usr/bin/python
# -*- coding: UTF-8 -*-


# a = input().split()
# num = int(a[0])
# file = a[1]
import random, sys

num = int(sys.argv[1])
file = sys.argv[2]

fo = open(file, 'w')
for x in range(num):
    # fo.write
    s = (str(random.randint(0, 99)) + random.choice('+-*/') + str(random.randint(1, 99)) + '\n')
    print(s,file=fo)
fo.close()
