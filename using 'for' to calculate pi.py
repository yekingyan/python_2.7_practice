﻿#-------------------------------------------------------------------------------
# Name:        for
#puporse:      calculate pi
#练习重点:     for in range
# Created:     27/04/2018
#coding:       utf-8
#-------------------------------------------------------------------------

pi = 0
a = 1
b = 1
for i in range(1,10000000,1):
    pi +=4.0 * a / b
    a *= -1
    b += 2
print pi