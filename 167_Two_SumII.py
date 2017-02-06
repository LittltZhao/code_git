# -*-coding:utf-8 -*-
# 排序列表取两个数使得两个数的和等于给定的数字
#解决方案：两头逼近
def twosum(numbers,target):
    lens=len(numbers)
    i,j=0,lens-1
    while i<j:
        x=numbers[i]+numbers[j]
        if x>target:
            j-=1
        elif x<target:
            i+=1
        else:
            return [i+1,j+1]
            break
print twosum([0,9,11,15],26)
