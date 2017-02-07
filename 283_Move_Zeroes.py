# -*- coding:utf-8 -*-
def moveZeroes(nums):
    index=0
    for i in range(len(nums)):
        if nums[i]!=0:#不等于零的直接向前移动
            nums[index]=nums[i]
            index+=1
        i+=1
    while index<len(nums):#身下最后的都赋值为0
        nums[index]=0
        index+=1



num=[1,0,0,4,1,5,0]
moveZeroes(num)
print num
