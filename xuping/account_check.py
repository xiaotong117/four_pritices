#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import time
import win32api
from xuping.db_interaction import get_db_price
from xuping.get_third_data import get_third_price
from xuping.compare import compare

if __name__ == "__main__":
    nowtime = time.strftime("%Y-%m-%d", time.localtime())
    file = '业务金额核对' + nowtime +'.xlsx'
    break_flag = 1
    print('************************************')
    print('*********滴滴订单数据校验系统********')
    print('************************************')
    while break_flag:
        time.sleep(1)
        print('\n请输入操作代码：\n1、预加载数据；2、数据校验；3、查看结果；4、退出系统')
        a = input()
        if a == '1':
            try:
                get_db_price(file)
                get_third_price(file)
                print('数据加载成功！')
            except:
                print('哎呀，出错了！')
        if a == '2':
            try:
                compare(file)
                print('数据校验成功！')
            except:
                print('哎呀，出错了！')
        if a == '3':
            try:
                win32api.ShellExecute(0, 'open', file, '', '', 1)
            except:
                print('哎呀，出错了！')
        if a == '4':
            break_flag = 0
