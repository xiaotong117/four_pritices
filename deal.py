#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import random, sys, operator

def make_poker():
    '''扑克牌生成、乱序、发牌'''
    a = [[x, y] for x in ['红心', '黑桃', '方块', '梅花'] for y in ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                                                            '10', 'J', 'Q', 'K']]
    # for x in range(52):
    #     rad = random.randint(x, 51)
    #     s = a[x]
    #     a[x] = a[rad]
    #     a[rad] = s

    random.shuffle(a)
    return a


def sort_num(list):
    '''扑克牌按大小排序'''
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
            return 10
        elif 'J' in a:
            return 11
        elif 'Q' in a:
            return 12
        elif 'K' in a:
            return 13


    # list.sort(cmp=shuzi)
    # sorted(list,key=shuzi)
    list.sort(key=shuzi)

    return list


    # for x in range(len(list)):
    #     if "A" in list[x]:
    #         s1 = list[x]
    #         list[x] = list[0]
    #         list[0] = s1
    #         continue
    #     for y in range(x+1,len(list)):
    #         if list[x] > list[y]:
    #             s2 = list[x]
    #             list[x] = list[y]
    #             list[y] = s2
    #             continue
    # return list

def sort(list):
    '''排序：将玩家手中扑克牌按花色大小整理好（黑桃>红心>梅花>方块）'''
    aa = []
    bb = []
    cc = []
    dd = []
    for x in list:
        if "黑桃" in x:
            aa.append(x)
        elif "红心" in x:
            bb.append(x)
        elif "梅花" in x:
            cc.append(x)
        elif "方块" in x:
            dd.append(x)
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
