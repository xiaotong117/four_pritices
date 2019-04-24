#!/usr/bin/python
# -*- coding: UTF-8 -*- 

'''
实现一个生成扑克牌小程序，例如执行 Python poker.py ,能打印出52张扑克牌，每项是一个列表，样式如下：
[['黑桃',A],['红心',2], …, ['梅花',K],['方块',K]]。
'''
# def pokepai():
# #     a = []
# #     for s in ['红桃', '黑桃', '方块', '梅花']:
# #         for x in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
# #             a.append([s, x])
# #     return a
# #
# # def pokepai2():
# #     return [[x, y] for x in ['红桃', '黑桃', '方块', '梅花'] for y in ['A', '2', '3', '4', '5', '6', '7', '8', '9',
# #                                                                '10', 'J', 'Q', 'K']]
# # if __name__ == '__main__':
# #     print('扑克牌列表为：', pokepai2())

def produce_poker():
    poker_item = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    poker_color = ['黑桃', '红心', '梅花', '方块']
    poker = []
    for item in poker_item:
        for i in zip(poker_color, [item] * 4):
            group = list(i) # i为元组，据需求转换为列表
            poker.append(group)
# print(poker)
    return poker


if __name__ == '__main__':
    print(produce_poker())