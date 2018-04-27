#-------------------------------------------------------------------------------
# Name:        while
#puporse:      1+2+3+...+
#练习重点:     while raw_input
# Created:     27/04/2018
#coding:       utf-8
#-------------------------------------------------------------------------

a = 1
s = 0
b = int(raw_input('enter a number to caccumulate:'))
while a < b + 1:
    s += a
    a += 1
print '%d time\'s sum is %d' % (a-1 , s)