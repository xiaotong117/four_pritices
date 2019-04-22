#!/usr/bin/python
# -*- coding: UTF-8 -*-

def bubb_sort(list):
    for x in range(len(list)-1):
        for y in range(len(list)-1-x):
            if list[y] > list[y+1]:
                s = list[y]
                list[y] = list[y+1]
                list[y + 1] = s
                # list[y],list[y+1] = list[y+1],list[y]
    return list

a = [23,43,13,3,64,45]
print(bubb_sort(a))