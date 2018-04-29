#-------------------------------------------------------------------------------
# Name:        回文数 质数
# Created:     29/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------

def judgingprime(x):#定义一个判断素数的函数
    """
    返回对X是否为素数的布尔值
    """
    if x % 2 == 0 and x != 2: #除了2的偶数不为素数
        return False
    else:
        for i in (range(2,x)):
            if x % i == 0:
                return False
        else:
            return True#是质数则返回True

def judgingpalin(x):#定义一个判断回文数的函数
    """
    返回对X是否为回文数的布尔值
    """
    t = x #储存输入值
    num_p = 0
    while x != 0:
        num_p = x % 10 + num_p * 10#左移加上求余
        x = x / 10 #整型,除个位数所有数右移一位,最后num变为0，结束循环
        # print x , num_p #查看运算逻辑
    if t == num_p:
        return True
    else:
        return False

x = int(raw_input(u'输入一个数:'))
if judgingprime(x) == True:#x为素数
    if judgingpalin(x) == True:#同时x为回文数
        print '%d is a prime and palindrome' % x
    else:
        print '%d is a prime , %d is\'t a palindrome number' % (x,x)
else:#x不为素数
    if judgingpalin(x) == True:#x为回文数
        print '%d isn\'t prime , %d is a palindrome number' % (x,x)
    else:#x不为回文数
        print '%d is not a palindrome number and prime' % x


