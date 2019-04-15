#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 'aa'
# def ss():
#     a.join('ss')
# print(a)

a = [1,1,1,1,1,1,1,1,1,1,1]
def Fuc():
    global a
    a = a+[2]
    print(id(a))
#    print(id(a[0]))
if __name__ == "__main__":
    print(id(a))
    for i in range(10):
        Fuc()
    print(a)
    print(id(a))


a = [1,2,3]


'K'>'J'
