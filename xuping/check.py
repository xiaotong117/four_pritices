#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl
from xuping import tools
from openpyxl.styles import PatternFill

def compare(file):
    wb = openpyxl.load_workbook(file)
    ws1 = wb.get_sheet_by_name('测试数据')
    ws2 = wb.get_sheet_by_name('预期数据')
    dict1 = tools.pull(ws1)
    dict2 = tools.pull(ws2)
    mail_flag = 0
    contant = []

    dict1['99999999999999999'] = 123
    dict2['99999999999999999'] = 12345

    ws = wb.create_sheet()
    ws.title = '数据校验结果'
    ws.append(['订单号', '订单表价格', '第三方价格', '校验结果'])

    for k in list(dict1.keys()):
        if k in dict2:
            if dict1[k] == dict2[k]:
                ws.append([k, dict1[k], dict2[k], '校验成功'])
                del dict1[k]
                del dict2[k]
            else:
                ws.append([k, dict1[k], dict2[k], '校验失败'])
                ws.cell(ws.max_row,4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
                mail_flag = 1
                contant.append(k)
                del dict1[k]
                del dict2[k]
        else:
            ws.append([k, dict1[k], 'Null', '校验失败'])
            ws.cell(ws.max_row, 4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
            mail_flag = 1
            contant.append(k)
    if dict2:
        for k in dict2.keys():
            ws.append([k, 'Null', dict2[k], '校验失败'])
            ws.cell(ws.max_row, 4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
            mail_flag = 1
            contant.append(k)

    tools.sheet_layout(ws)
    for col in ['A', 'B', 'C', 'D']:
        ws.column_dimensions[col].width = 30

    wb.save(file)

    if mail_flag:
        text = ''
        for x in contant:
            text += x + '\n'
        message = '下列订单对账出错：\n'+ text + '\n详情请查看业务金额核对脚本结果！'
        tools.mail('zhangt@shinemo.com', message, '对账出错了！')


class check_status(object):
    def __init__(self, order_list):
        self.order_list = order_list

    def check_20001(self, order_list):
        for order in order_list:




