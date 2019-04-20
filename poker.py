#!/usr/bin/python
# -*- coding: UTF-8 -*- 

def pokepai():
    a = []
    for s in ['红桃', '黑桃', '方块', '梅花']:
        for x in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            a.append([s, x])
    return a

def pokepai2():
    return [[x, y] for x in ['红桃', '黑桃', '方块', '梅花'] for y in ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                                                               '10', 'J', 'Q', 'K']]
if __name__ == '__main__':
    print('扑克牌列表为：', pokepai2())