#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''数据库连接配置'''
DB_CONFIG_BUY = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'buy'
}

DB_CONFIG_WELFARE = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'welfare'
}

'''订单表数据SQL查询语句'''
SQL_order_price = 'select order_id,source_app,price,update_user_name,gmt_create ' \
                  'from buy_order_new where biz_type = 3 and order_sub_status = %s ' \
                  'order by id desc'

'''第三方数据SQL查询语句'''
SQL_third_data = 'select order_id,price,update_user_name,gmt_pay from buy_order_new where biz_type = 3 ' \
                  'and order_status = 12'

'''拉取buy_order_new数据'''
SQL_buy_order_new = 'select order_id,order_type,order_status,third_id,price from buy_order_new where order_id = \'%s\''

'''拉取car_order数据'''
SQL_car_order = 'select biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name ' \
                'from car_order where order_id = \'%s\''

'''拉取tc.user_frezen_detail数据'''
SQL_user_frezen_detail = ''

'''拉取shinemo_welfare.account_freeze数据'''
SQL_account_freeze = ''

