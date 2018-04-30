#-------------------------------------------------------------------------------
# Name:        日历
# Created:     30/04/2018
# coding:       utf-8
#问题:          第一行无法对齐
#-------------------------------------------------------------------------------
'''
import calendar
year = raw_input('year:')
month = raw_input('month:')
print calendar.month(year,month)
'''




year = int(raw_input(u'请输入年份:'))
month = int(raw_input(u'请输入月份:'))


#输出日历头部
month_drit = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

print '         ',month_drit[month],'       ',
print year
print '-------------------------------------'
print '  SUN  Mon  Tue  Wed  Thu  Fri  Sat'



#
def is_leap_year(year):
    '''
    判断是否为闰年
    '''
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_number_of_days_in_mounth(year,month):
    '''
    获取该月有多少天
    '''
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year) == True:
        return 29
    else:
        return 28

def get_total_num_of_days(year,month):
    '''
    自1800年1月1日一共多少天
    '''
    days = 0
    for y in range(1800,year):
        if is_leap_year(y) == True:
            days += 366
        else:
            days += 365
    for m in range(1,month):
        days += get_number_of_days_in_mounth(year,m)
    return days

def get_start_day(year,month):
    '''
    1号星期几
    '''
    return (3 + get_total_num_of_days(year,month)) % 7


def print_month_body(year,month):

    #打印日历部份

    i = get_start_day(year,month)
    if i != 7:
        print ' ',
        print '    ' * i,
    for j in range(1,get_number_of_days_in_mounth(year,month) + 1):
        print '%4d' % j,
        i += 1
        if i % 7 == 0:
            print ' '

#输出日历内容
print_month_body(year,month)


