#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = [['梅花', '10'], ['梅花', 'Q'], ['梅花', '4']]
a.sort()
print(a)
def shuzi(a):
    if 'A' in a:
        return 1
    elif '2' in a:
        return 2
    elif '3' in a:
        return 3
    elif '4' in a:
        return 4
    elif '5' in a:
        return 5
    elif '6' in a:
        return 6
    elif '7' in a:
        return 7
    elif '8' in a:
        return 8
    elif '9' in a:
        return 9
    elif '10' in a:
        # print(10)
        return 10
    elif 'J' in a:
        return 11
    elif 'Q' in a:
        return 12
    elif 'K' in a:
        return 13

a.sort(key=shuzi)
print(a)