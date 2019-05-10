#!/usr/bin/python
# -*- coding: UTF-8 -*-

# basket = {'apple'}
# basket=set("apple")
# print(basket[0])

import os
def open_app(app_dir):
    os.startfile(app_dir)
if __name__ == "__main__":
    app_dir = r'C:\Users\Administrator\PycharmProjects\four_pritices\xuping\abc.xlsx'
    open_app(app_dir)