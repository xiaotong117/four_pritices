#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl
import time
import logging
import win32api
from openpyxl.styles import PatternFill
from xuping.db_interaction import get_db_price
from xuping.check import check_status
from xuping import tools

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
                print('数据加载成功！')
            except:
                logging.error("哎呀，出错了！", exc_info=True)
        if a == '2':
            try:
                wb = openpyxl.load_workbook(file)
                ws = wb.create_sheet()
                ws.title = '数据校验结果'
                ws.append(['订单号', '出错字段'])
                ws1 = wb.get_sheet_by_name('订单状态20001')
                list1 = [ws1.cell(x, 1).value for x in range(2, ws1.max_row + 1)]
                false = check_status.check_base(list1) + check_status.check_20001(list1)
                print('校验状态20001数据%s条。'%(len(list1)))
                print('其中%s条数据异常。'%(len(list1)))
                for k in list(false.keys()):
                    ws.append([k, false[k]])

                '''拉数据时，增加对数据为空时的处理'''



                tools.sheet_layout(ws)
                for col in ['A', 'B']:
                    ws.column_dimensions[col].width = 30

                wb.save(file)



            except:
                logging.error("哎呀，出错了！", exc_info=True)
        if a == '3':
            try:
                win32api.ShellExecute(0, 'open', file, '', '', 1)
            except:
                logging.error("哎呀，出错了！", exc_info=True)
        if a == '4':
            break_flag = 0
