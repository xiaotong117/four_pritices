#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl
from xuping import config
from openpyxl.styles import PatternFill

def compare(file):
    wb = openpyxl.load_workbook(file)
    ws1 = wb.get_sheet_by_name('订单表数据')
    ws2 = wb.get_sheet_by_name('第三方数据')
    dict1 = config.pull(ws1)
    dict2 = config.pull(ws2)

    dict1['故意错的'] = 123
    dict2['故意错的'] = 12345

    ws = wb.create_sheet()
    ws.title = '数据校验结果'
    ws.append(['订单号', '订单表价格', '第三方价格', '校验结果'])

    for k in dict1.keys():
        if dict1[k] == dict2[k]:
            ws.append([k, dict1[k], dict2[k], '校验成功'])
        else:
            ws.append([k, dict1[k], dict2[k], '校验失败'])
            ws.cell(ws.max_row,4).fill = PatternFill(fill_type='solid', fgColor='FF0000')

    config.sheet_layout(ws)
    for col in ['A', 'B', 'C', 'D']:
        ws.column_dimensions[col].width = 30

    wb.save(file)


