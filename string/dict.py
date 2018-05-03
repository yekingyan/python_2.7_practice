#-------------------------------------------------------------------------------
# Name:        词频统计
# Created:     3/05/2018
# coding:       utf-8
#-------------------------------------------------------------------------------

f = open('emma.txt','r')

word_freq = {}
for line in f:
    words = line.strip().split()#去空格 分割字符存在列表中
    for word in words:#统计word出现次数
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1



freq_word = []
for word,freq in word_freq.items():
    freq_word.append((freq,word))#插入元素

freq_word.sort(reverse = True)#降序排序

for freq,word in freq_word[:10]:#到前十个
    print word
f.close()

