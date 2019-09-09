#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import openpyxl
import logging
from xuping import tools,config
from openpyxl.styles import PatternFill

# def compare(file):
#     wb = openpyxl.load_workbook(file)
#     ws1 = wb.get_sheet_by_name('测试数据')
#     ws2 = wb.get_sheet_by_name('预期数据')
#     dict1 = tools.pull(ws1)
#     dict2 = tools.pull(ws2)
#     mail_flag = 0
#     contant = []
#
#     dict1['99999999999999999'] = 123
#     dict2['99999999999999999'] = 12345
#
#     ws = wb.create_sheet()
#     ws.title = '数据校验结果'
#     ws.append(['订单号', '订单表价格', '第三方价格', '校验结果'])
#
#     for k in list(dict1.keys()):
#         if k in dict2:
#             if dict1[k] == dict2[k]:
#                 ws.append([k, dict1[k], dict2[k], '校验成功'])
#                 del dict1[k]
#                 del dict2[k]
#             else:
#                 ws.append([k, dict1[k], dict2[k], '校验失败'])
#                 ws.cell(ws.max_row,4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
#                 mail_flag = 1
#                 contant.append(k)
#                 del dict1[k]
#                 del dict2[k]
#         else:
#             ws.append([k, dict1[k], 'Null', '校验失败'])
#             ws.cell(ws.max_row, 4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
#             mail_flag = 1
#             contant.append(k)
#     if dict2:
#         for k in dict2.keys():
#             ws.append([k, 'Null', dict2[k], '校验失败'])
#             ws.cell(ws.max_row, 4).fill = PatternFill(fill_type='solid', fgColor='FF0000')
#             mail_flag = 1
#             contant.append(k)
#
#     tools.sheet_layout(ws)
#     for col in ['A', 'B', 'C', 'D']:
#         ws.column_dimensions[col].width = 30
#
#     wb.save(file)
#
#     if mail_flag:
#         text = ''
#         for x in contant:
#             text += x + '\n'
#         message = '下列订单对账出错：\n'+ text + '\n详情请查看业务金额核对脚本结果！'
#         tools.mail('zhangt@shinemo.com', message, '对账出错了！')


class check_status(object):
    def __init__(self, order_list):
        self.order_list = order_list

    def check_base(order_list):
        for order in order_list:
            #校验buy_order_new
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_buy_order_new1], order)
            a = b_data[0]
            if a[1] == 0:
                if a[0]==2 and a[2]!= '' and a[3]!= 0:
                    pass
                else:
                    print("buy_order_new表校验失败！")
                    continue
            elif a[1] == -1:
                if a[0] == 2 and a[2] != '' and a[3] != 0:
                    pass
                else:
                    print("buy_order_new表校验失败！")
                    continue
            else:
                print('订单\'%s\'状态错误！'% order)
                continue

            # 校验冻结表
            if a[1] == -1:
                pass
            else:
                if a[4] == 0:
                    t_data = tools.pull_data(config.DB_CONFIG_TC, [config.SQL_user_frezen_detail, config.SQL_pay_detail],
                                            order)
                    c = t_data[0]
                    if c[0] == 3 and c[1] == a[3] and a[2] == 1:
                        pass
                    else:
                        print('user_frezen_detail表校验失败！')
                        continue

                elif a[4] == 8:
                    w_data = tools.pull_data(config.DB_CONFIG_WELFARE,
                                            [config.SQL_account_freeze, config.SQL_welfare_turnover], order)
                    c = w_data[0]
                    if c[0] == a[3]*1.5 and c[1] == 1:
                        pass
                    else:
                        print('account_freeze表校验失败！')
                        continue

                elif a[4] == 13:
                    w_data = tools.pull_data(config.DB_CONFIG_WELFARE,
                                            [config.SQL_account_freeze, config.SQL_welfare_turnover], order)
                    c = w_data[0]
                    if c[0] == a[3]*2 and c[1] == 1:
                        pass
                    else:
                        print('account_freeze表校验失败！')
                        continue

                else:
                    print('订单\'%s\'类型错误！' % order)
                    continue

    def check_20001(order_list):
        for order in order_list:
            # 校验car_order
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_car_order1], order)
            b = b_data[0]
            if b[0] == 3 and all(x != '' for x in b):
                pass
            else:
                print('car_order表校验失败！')
                continue

    def check_20003(order_list):
        for order in order_list:
            # 校验car_order
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_car_order2], order)
            b = b_data[0]
            if b[0] == 3 and all(x != '' for x in b):
                pass
            else:
                print('car_order表校验失败！')
                continue

    def check_20007(order_list):
        for order in order_list:
            # 校验car_order
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_car_order3], order)
            b = b_data[0]
            if b[0] == 3 and all(x != '' for x in b):
                pass
            else:
                print('car_order表校验失败！')
                continue

    def check_20009(order_list):
        for order in order_list:
            # 校验car_order
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_car_order4], order)
            b = b_data[0]
            if b[0] == 3 and all(x != '' for x in b):
                pass
            else:
                print('car_order表校验失败！')
                continue

    def check_20017(order_list):
        for order in order_list:
            # 校验car_order
            b_data = tools.pull_data(config.DB_CONFIG_BUY, [config.SQL_buy_order_new2, config.SQL_car_order5], order)
            b = b_data[1]
            if b[0] == 3 and all(x != '' for x in b):
                pass
            else:
                print('car_order表校验失败！')
                continue

            a = b_data[0]
            if a[9] == 0:
                if a[0]==2 and a[1]==1 and a[2]==12 and a[3]!="" and a[4]!="" and a[5]!="" and a[6]!=0 and a[7]!=0:
                    pass
                else:
                    print("buy_order_new表校验失败！")
                    continue

            elif a[9] == 8 or a[9] == 13:
                if a[0]==2 and a[1]==1 and a[2]==12 and a[3]!="" and a[4]!="" and a[5]!="" and a[6]!=0 and a[8]!=0:
                    pass
                else:
                    print("buy_order_new表校验失败！")
                    continue


a = check_status.check_20003(['010031904020000004358836'])







