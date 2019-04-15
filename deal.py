#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import random, sys

def make_poker():
    '''扑克牌生成、乱序、发牌'''
    a = [[x, y] for x in ['红心', '黑桃', '方块', '梅花'] for y in ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                                                            '10', 'J', 'Q', 'K']]
    for x in range(52):
        rad = random.randint(x, 51)
        s = a[x]
        a[x] = a[rad]
        a[rad] = s
    return a


def sort_num(list):
    '''扑克牌按大小排序'''
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            if "A" in list[x]:
                s1 = list[x]
                list[x] = list[0]
                list[0] = s1
                continue

            elif list[x] > list[y]:
                s2 = list[x]
                list[x] = list[y]
                list[y] = s2
                continue
    return list

def sort(list):
    '''排序：将玩家手中扑克牌按花色大小整理好（黑桃>红心>梅花>方块）'''
    aa = []
    bb = []
    cc = []
    dd = []
    for x in list:
        if "黑桃" in x:
            aa.append([x])
        elif "红心" in x:
            bb.append([x])
        elif "梅花" in x:
            cc.append([x])
        elif "方块" in x:
            dd.append([x])
    # print(aa)
    return sort_num(aa)+sort_num(bb)+sort_num(cc)+sort_num(dd)


if __name__ == '__main__':
    pokepai = make_poker()
    print('洗牌后：', pokepai)

    print('玩家1的牌', pokepai[:13])
    print('玩家2的牌', pokepai[13:26])
    print('玩家3的牌', pokepai[26:39])
    print('玩家4的牌', pokepai[39:52])


    print('玩家1整理后的牌', sort(pokepai[:13]))
    print('玩家2整理后的牌', sort(pokepai[13:26]))
    print('玩家3整理后的牌', sort(pokepai[26:39]))
    print('玩家4整理后的牌', sort(pokepai[39:52]))
