#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xuping import config
import pymysql, openpyxl

conn = pymysql.connect(**config.DB_CONFIG)
cursor = conn.cursor()

try:
    cursor.execute(config.SQL_order_price)
    results = cursor.fetchall()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = '订单表数据'
    ws.append(['订单号', '订单金额', '下单人', '支付时间',])

    for row in results:
        ws.append(row)
        # print(row)

except:
   print ("Error: unable to fetch data")


conn.close()
wb.save('业务金额核对.xlsx')