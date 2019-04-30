#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import time, pickle,os

'''
题目：生成100个银行卡卡号，卡号以6102009开头， 后面3位依次是 （001， 002， 003 …… 100），默认每个卡号的初始密码为"admin123"，
输入卡号和密码信息， 判断是否登录成功。在上题的基础上，登录成功后可以进行账户余额查询、存款、取款、转账、修改密码、
注销账户的功能，输出一个完整的银行卡系统。
'''

def make_card():
    card = {}
    card_info = {}
    front = '6102009'
    for x in range(1,101):
        ID = front + str('%03d'% x)
        card[ID] = 'admin123'
        card_info[ID] = 0
    return card, card_info

def login_in(account,password,dict1):
    try:
        if dict1[account] == password:
            print('恭喜您登陆成功！')
            return 1
        else:
            print('登录失败！')
            return 0
    except:
        print("登录失败！")

def balance(dict2, account):
    print('您的账户余额为：', dict2[account])

def deposit(dict2, account):
    print('请输入存款金额：')
    amount = input()

    try:
        if float(amount) < 0:
            print('请输入正确的金额！')
            return 0
        dict2[account] += float(amount)
        print('存款成功！')
        return 1
    except:
        print('请输入正确的金额！')
        return 0

def withdraw(dict2, account):
    print('请输入取款金额：')
    amount = input()
    try:
        if float(amount) < 0:
            print('请输入正确的金额！')
            return 0
        if dict2[account] < float(amount):
            print('您的账户余额不足！')
            return 0
        else:
            dict2[account] -= float(amount)
            print('取款成功！')
            return 1
    except:
        print('请输入正确的金额！')
        return 0

def transfer(dict2, account):
    print('请输入转账账户：')
    account2 = input()
    if account2 not in dict2:
        print('请输入有效的转账账户！')
        return 0
    print('请输入转账金额：')
    amount = input()
    if float(amount)<0:
        print('请输入正确的金额！')
        return 0
    try:
        if dict2[account] >= float(amount):
            dict2[account] -= float(amount)
            dict2[account2] += float(amount)
            print('转账成功！')
            return 1
        else:
            print('您的余额不足！')
            return 0
    except:
        print('请输入正确的金额！')
        return 0

def change_pw(dict1,account):
    print('请输入旧密码：')
    old_pw = input()
    if dict1[account] == old_pw:
        print('请输入新密码：')
        new_pw1 = input()
        print('请再次输入新密码：')
        new_pw2 = input()
        if new_pw1 == new_pw2:
            dict1[account] = new_pw1
            print('密码修改成功！')
            return 1
        else:
            print('两次输入的新密码不一致！')
            return 0

    else:
        print('旧密码错误！')
        return 0

def check_info(dict1, dict2, account):
    print('您确定要注销银行卡吗？y/n')
    sure = input()
    if sure == 'y':
        del dict1[account]
        del dict2[account]
        return 1
    else:
        return 0


if __name__ == '__main__':
    print('\n*******************************************')
    print('************欢迎进入渣渣银行系统************')
    print('*******************************************\n')
    print("请输入卡号和密码，进行登录：")
    if os.path.exists('dict1.pickle') and os.path.exists('dict1.pickle'):
        with open('dict1.pickle', 'rb') as f:
            dict1 = pickle.load(f)
        with open('dict2.pickle', 'rb') as f:
            dict2 = pickle.load(f)
    else:
        dict1, dict2 = make_card()

    account = input()
    password = input()
    if login_in(account,password,dict1):
        break_flag = 1
        while break_flag:
            time.sleep(1)
            print('\n*********请输入要进行的操作序号：*********\n'
                  '  1.余额查询     5.修改密码\n  2.存款         6.注销账户\n  3.取款         7.退出\n  4.转账')
            a = input()
            if a == '1':
                balance(dict2, account)
            elif a == '2':
                deposit(dict2, account)
            elif a == '3':
                withdraw(dict2, account)
            elif a == '4':
                transfer(dict2, account)
            elif a == '5':
                change_pw(dict1, account)
            elif a == '6':
                if check_info(dict1, dict2, account):
                    break_flag = 0
                    break
            elif a == '7':
                break_flag = 0
                break
            else :print('请输入有效的操作序列！')


        with open('dict1.pickle', 'wb') as f:
            pickle.dump(dict1, f)
        with open('dict2.pickle', 'wb') as f:
            pickle.dump(dict2, f)



