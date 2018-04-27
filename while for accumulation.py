#-------------------------------------------------------------------------------
# Name:        while
#puporse:      1+2+3+...+
#练习重点:     while break
# Created:     27/04/2018
#coding:       utf-8
#-------------------------------------------------------------------------

a = 1
s = 0
while True:
    s += a
    a += 1
    print '%d time\'s sum is %d',(a-1 , s)
    if raw_input('anwer \'q\' to quit:'):
        break
