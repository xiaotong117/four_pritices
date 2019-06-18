#!/usr/bin/python
# -*- coding: UTF-8 -*-




class Myclass(object):
    def __init__(self, x):
        self.x = x


c1 = Myclass(11)
c2 = Myclass.__new__(Myclass, 12)
print(c1.x, c2.x)