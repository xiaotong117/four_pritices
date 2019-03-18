#!/usr/bin/python

import time

name = input()
time = time.strftime("%H:%M:%S %p", time.localtime())

print("Hello " + name + ",it's " + time + "now!")