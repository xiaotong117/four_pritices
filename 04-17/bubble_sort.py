#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：用python实现冒泡排序算法（可视化算法解析https://visualgo.net/zh/sorting?slide=1）
'''

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