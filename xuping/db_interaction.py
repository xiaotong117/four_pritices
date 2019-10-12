#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xuping import tools,config
import logging
import openpyxl
import time

def get_db_price(file):
    try:
        wb = openpyxl.Workbook()
        db_buy = tools.db_connect(config.DB_CONFIG_BUY)
        for x in [20001, 20003, 20007, 20009, 20017, 20019, 20021]:
            ws = wb.create_sheet()
            ws.title = '订单状态' + str(x)
            ws.append(['订单号', '订单类型', '订单金额', '下单人', '下单时间'])

            start = time.time()
            for row in tools.pull_data(db_buy, [config.SQL_order_price], x):
                ws.append(row)
            end = time.time()
            print('x：' + str(end - start))

            tools.sheet_layout(ws)
            for col in ['A', 'B', 'C', 'D', 'E']:
                ws.column_dimensions[col].width = 30

        tools.db_disconnect(db_buy)
        wb.remove_sheet(wb.get_sheet_by_name("Sheet"))
    except:

        logging.error("Error: unable to fetch data", exc_info=True)

    wb.save(file)

# file = '业务金额核对2019-05-09.xlsx'
# get_db_price(file)