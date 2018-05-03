#-------------------------------------------------------------------------------
# Name:        平均数 average
# Created:     1/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------

nums = []
for i in range(10):
    nums.append(float(raw_input('input numbers:')))

s = 0
'''
for num in nums:
    s += num
avg = s / len(nums)
'''
avg = sum(nums) / len(nums)
print avg