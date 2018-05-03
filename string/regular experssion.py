#-------------------------------------------------------------------------------
# Name:        正则表达判断人名
# Created:     1/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------

import re#引用正则表达式
f = open('names.txt','r')



for a in f:
    a = a.strip()
    pattern = 'C.A'
    result = re.search(pattern,a)#搜录匹配
    if result:#如果有返回值
        print a


f.close()