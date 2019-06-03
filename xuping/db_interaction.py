#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xuping import config, tools
import pymysql, openpyxl

def get_db_price(file):
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = '测试数据'
        ws.append(['订单号', '订单类型', '订单金额', '下单人', '下单时间'])

        for row in tools.pull_data(20001):
            ws.append(row)

        tools.sheet_layout(ws)
        for col in ['A', 'B', 'C', 'D']:
            ws.column_dimensions[col].width = 30

    except:
        print ("Error: unable to fetch data")

    wb.save(file)

file = '业务金额核对2019-05-09.xlsx'
get_db_price(file)