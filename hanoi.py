#-------------------------------------------------------------------------------
# Name:        汉诺塔 honoi
# Created:     1/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------
count = 0
def hanoi (n,A,B,C):
    global count
    if n == 1:
        print 'move',n,'form',A,'to',C
        count +=1
    else:
        hanoi(n - 1,A,C,B)
        print 'move',n,'form',A,'to',C
        count += 1
        hanoi(n - 1,B,A,C)

n = int(raw_input('n:'))
hanoi(n,'left','mid','right')
print count