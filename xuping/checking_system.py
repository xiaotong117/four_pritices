#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl
import time
import logging
import win32api
from xuping.db_interaction import get_db_price
from xuping.check import check_status
from xuping import tools

if __name__ == "__main__":
    nowdate = time.strftime("%Y-%m-%d", time.localtime())
    file = '业务金额核对' + nowdate +'.xlsx'
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
                ws.title = '数据校验结果' + time.strftime("%H-%M-%S", time.localtime())
                ws.append(['订单子状态','订单号', '出错字段'])

                for x in ('20001', '20003', '20007', '20009'):
                    ws1 = wb.get_sheet_by_name('订单状态%s'% x)
                    listx = [ws1.cell(x, 1).value for x in range(2, ws1.max_row + 1)]
                    false = check_status.check_base(listx)
                    c = {'20001':check_status.check_20001(listx), '20003':check_status.check_20003(listx), '20007':check_status.check_20007(listx), '20009':check_status.check_20009(listx)}[x]
                    false.update(c)
                    print('校验状态%s数据%s条。'%(x, len(listx)))
                    print('其中%s条数据异常。\n'%(len(false)))
                    for k in list(false.keys()):
                        ws.append([x, k, false[k]])

                for x in ('20017', '20019', '20021'):
                    ws1 = wb.get_sheet_by_name('订单状态%s'% x)
                    listx = [ws1.cell(x, 1).value for x in range(2, ws1.max_row + 1)]
                    false = {'20017':check_status.check_20017(listx), '20019':check_status.check_20019(listx), '20021':check_status.check_20021(listx)}[x]
                    print('校验状态%s数据%s条。'%(x, len(listx)))
                    print('其中%s条数据异常。\n'%(len(false)))
                    for k in list(false.keys()):
                        ws.append([x, k, false[k]])

                # ws1 = wb.get_sheet_by_name('订单状态20021')
                # listx = [ws1.cell(x, 1).value for x in range(2, ws1.max_row + 1)]
                # false = check_status.check_20021(listx)
                # print('校验状态20021数据%s条。' % (len(listx)))
                # print('其中%s条数据异常。\n' % (len(false)))
                # for k in list(false.keys()):
                #     ws.append(['20021', k, false[k]])

                tools.sheet_layout(ws)
                for col in ['A', 'B', 'C']:
                    ws.column_dimensions[col].width = 40

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
