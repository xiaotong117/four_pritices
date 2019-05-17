#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xuping import config, tools
import pymysql, openpyxl

def get_db_price(file):
    conn = pymysql.connect(**config.DB_CONFIG)
    cursor = conn.cursor()

    try:
        cursor.execute(config.SQL_order_price)
        results = cursor.fetchall()

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = '测试数据'
        ws.append(['订单号', '订单金额', '下单人', '支付时间'])

        for row in results:
            ws.append(row)

        tools.sheet_layout(ws)
        for col in ['A', 'B', 'C', 'D']:
            ws.column_dimensions[col].width = 30

    except:
        print ("Error: unable to fetch data")


    conn.close()
    wb.save(file)

# file = '业务金额核对2019-05-09.xlsx'
# get_db_price(file)