#-------------------------------------------------------------------------------
# Name:        鸡兔同笼
#练习重点:     for
# Created:     27/04/2018
#coding:       utf-8
#-----------------------------------------------------------------------

#Party 1 方程
heads = int(raw_input('how many heads?:'))
legs = int(raw_input('how many legs?:'))
for chickens in range(heads + 1):
    rabbits = heads - chickens
    if  legs == 2 * chickens + 4 * rabbits:
        print '%d chickens an1d %d rabbits' % (chickens,rabbits)
'''

#Party 2 穷举
for chickens in range(35+1):
    for rabbits in range(35+1):
        if chickens + rabbits == 35 and 2 * chickens + 4 * rabbits == 94:
                print '%d chickens and %d rabbits' % (chickens,rabbits)
'''
