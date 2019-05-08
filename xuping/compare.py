#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl

wb = openpyxl.load_workbook('业务金额核对.xlsx')
ws = wb.create_sheet()
ws.title = '第三方数据'
