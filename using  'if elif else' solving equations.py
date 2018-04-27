#-------------------------------------------------------------------------------
# Name:        计算一元二次方程根
#puporse:      求解ax^2 + bx = c
#练习重点:     if elif else
# Created:     22/04/2018
#-------------------------------------------------------------------------
import math#引用
a = float(raw_input("a:"))
if a == 0:
    print 'a can be zero'
elif a != 0:
    b = float(raw_input("b:"))
    c = float(raw_input("c:"))
    if b ** 2 - 4 * a * c == 0:
        print 's:',-b / 2 * a
    else:
        root = b ** 2 - 4 * a * c
        s1 = (-b + root) / (2 * a)
        s2 = (-b - root) / (2 * a)
        print 's1,s2 is', s1 , s2