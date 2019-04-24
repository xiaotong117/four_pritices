#!/usr/bin/python
# -*- coding: UTF-8 -*- 

'''
题目：生成100个银行卡卡号，卡号以6102009开头， 后面3位依次是 （001， 002， 003 …… 100），默认每个卡号的初始密码为"admin123"，
输入卡号和密码信息， 判断是否登录成功。
'''
card = {}
front = '6102009'
for x in range(1,101):
    ID = front + str('%03d'% x)
    card[ID] = 'admin123'

account = input('请输入卡号：')
password = input('请输入密码：')

try:
    if card[account] == password:
        print('恭喜您登陆成功！')
    else:
        print('登录失败！')
except:
    print("登录失败！")

