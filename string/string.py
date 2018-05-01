#-------------------------------------------------------------------------------
# Name:         文本信息的处理
# Created:     1/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------
'''
def vowles_count(s):
#判断字符串有多少个元音
    count = 0
    for c in s:
        if c in 'aeiouAEIOU':
            count += 1#累加统计
    return count
world  = raw_input('input worlds:')
print vowles_count(world)
'''

f = open('names.txt','r')#只读方式打开文件

def panlind(x):
# 判断名字是否回文
    low = 0
    high = len(x) - 1
    while low < high:
        if x[low] != x[high]:
            return False
        low += 1
        high -= 1
    return True

def panlind2(x):
#用递归的方法来判断名字是否是回文
    if len(x) <= 1:
        return True
    else:
        if x[0] != x[-1]:
            return False
        else:
            return panlind2(x[1:-1])

for line in f:
    line = line.strip()#删除多余换行
    if panlind2(line):#用panlind'或'panlind2'来判断叵名字是回文
        print line.title()#首字母大写,其它小写

f.close()#关闭文件