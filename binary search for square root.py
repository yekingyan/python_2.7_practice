#-------------------------------------------------------------------------------
# Name:        二分法求平方根 binary search for square root
#练习重点:     if else while abs
# Created:     27/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------

x = float(raw_input(u'求一个数的平方根:'))
if x < 1:
    print (u'二分法不能计算小于1的数')
else:
    low = 0.0
    number = x#加入这个变量是为了使变量X的值不再发生改变
    guess = (low + number) / 2
    while abs(x - guess ** 2) > 1e-10 :#相减绝对值确定精度

        if x > guess ** 2:
            low = guess
        else:
            number = guess
        guess = (low + number) / 2
    print round(guess,4)#四舍五入




