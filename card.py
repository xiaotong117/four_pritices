#!/usr/bin/python
# -*- coding: UTF-8 -*- 

def make_card(card={}):
    front = '6102009'
    for x in range(100):
        ID = front + str('%03d'% x)
        card[ID] = 'admin123'
    return card

def login_in(account,password,db):
    if db[account] == password:
        print('恭喜您登陆成功！')
        return 1
    else:
        print('登录失败，再见！')
        return 0

def change_pw(db,account,old_pw,new_pw):
    if db[account] == old_pw:
        db[account] = new_pw
        print('密码修改成功！')
        return 1
    else:
        print('旧密码错误！')
        return 0

if __name__ == '__main__':
    print('*******************************************')
    print('************欢迎进入渣渣银行系统************')
    print('*******************************************')
    print("请输入卡号和密码，进行登录：")
    db = make_card()
    account = input()
    password = input()
    if login_in(account,password,s):
        print('*********请输入要进行的操作序号：*********\n1.修改密码\n2.查询账号信息\n3.修改账号信息')
        a = input()
        if a == '1':
            print('请输入旧密码：')
            old_pw = input()
            print('请输入新密码：')
            new_pw1 = input()
            print('请再次输入新密码：')
            new_pw2 = input()
            if new_pw1 == new_pw2:
                change_pw(db,account,old_pw,new_pw1)
            else:print('两次输入的新密码不一致，再见！')
        elif a == 2:
            print('账号信息为xxxx')
        elif a == 3:
            print('请输入用户姓名和手机号')
        else:print('请输入有效的操作序号')



