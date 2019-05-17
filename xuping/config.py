#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''数据库连接配置'''
DB_CONFIG = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'buy'
}

'''订单表数据SQL查询语句'''
SQL_order_price = 'select order_id,price,update_user_name,gmt_pay from buy_order_new where biz_type = 3 ' \
                  'and order_status = 12 order by id desc'

'''第三方数据SQL查询语句'''
SQL_third_data = 'select order_id,price,update_user_name,gmt_pay from buy_order_new where biz_type = 3 ' \
                  'and order_status = 12'

