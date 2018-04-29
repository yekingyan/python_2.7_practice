#-------------------------------------------------------------------------------
# Name:        回文数 质数
# Created:     29/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------

def judgingprime(x):#定义一个判断质数的函数
    if x % 2 == 0 and x != 2: #除了2的偶数不为素数
        return False
    else:
        for i in (range(2,x)):
            if x % i == 0:
                return False
        else:
            return True#是质数则返回True


num = int(raw_input(u'输入一个数:'))
t = num #储存输入值
num_p = 0
while num != 0:
    num_p = num % 10 + num_p * 10#左移加上求余
    num = num / 10 #整型,除个位数所有数右移一位,最后num变为0，结束循环
    # print num , num_p #查看运算逻辑
if t == num_p:
    if judgingprime(t) == True:
        print 'Also,%d is a prime' % t
    else:
        print 'Although %d is not prime , %d is a palindrome number' % (t,t)
elif judgingprime(t) == True:
    print '%d is prime , %d is not a palindrome number'
else:
    print '%d is not a palindrome number and prime' % t


