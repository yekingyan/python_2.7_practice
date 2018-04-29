#-------------------------------------------------------------------------------
# Name:        回文数
# Created:     29/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------
num = int(raw_input(u'输入一个数:'))
t = num #储存输入值
num_p = 0
while num != 0:
    num_p = num % 10 + num_p * 10#左移加上求余
    num = num / 10 #整型,除个位数所有数右移一位,最后num变为0，结束循环
    # print num , num_p #查看运算逻辑
if t == num_p:
    print '%d is a palindrome number'
else:
    print '%d is not a palindrome number'