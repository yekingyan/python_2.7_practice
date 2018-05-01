#-------------------------------------------------------------------------------
# Name:        字符串比较，升序
# Created:     1/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------
f = open('names.txt','r')


def ascending(name):
#判断是否为升序
    p = name[0]
    for c in name:
        if p > c:
            return False
        else:
            p = c
    return True

def ascending2(name):
#用递归的方式判断升序
    if len(name) < 2:
        return True
    if name[0] > name[1]:
        return False
    else:
        return ascending2(name[1:])

for a in f:
    a = a.strip()
    if ascending2(a):
        print a