#-------------------------------------------------------------------------------
# Name:        素数 prime
# Created:     27/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------
'''
#素数的判断
x = int(raw_input(u'判断是否为素数:'))
if x % 2 == 0 and x != 2: #除了2的偶数不为素数
    print u'%d 不是素数' % x
else:

    for i in (range(2,x)):
        if x % i == 0:
            print u'%d 不是素数' % x
            break
    else:
        print u'%d 是素数' % x
'''
#找出前n个素数
import math
times = 0
number = 2
n = int(raw_input(u'按顺序找到n个素数，n:'))
while times < n:#找到n个素数停止
    for i in range(2,int(math.sqrt(number)) + 1):
        if number % i == 0:
            break
    else:
        print number
        times +=1 #计数累加
    number += 1

'''
问题
if number % i != 0:
    break 与 print number  交换后,无效
             times +=1
'''





