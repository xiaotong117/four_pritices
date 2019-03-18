#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

name = input()
time = time.strftime("%H:%M:%S %p", time.localtime())

print("Hello " + name + ",it's " + time + "now!")