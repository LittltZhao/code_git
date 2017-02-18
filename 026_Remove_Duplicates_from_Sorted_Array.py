# -*- coding:utf-8 -*-

def removeDuplicates(nums):
    i,pre=0,None
    while i<len(nums):#len(nums)是变化的，每进行一次判断都会重新计算
        if nums[i]!=pre:
            pre=nums[i]
            i+=1
        else:
            del nums[i]#del之后索引不会递增，因此索引不加一
    return len(nums)

def removeDuplicates2(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            del nums[i]
        else:
            i+=1
    return len(nums)

print removeDuplicates2([0,0,0,0,0])
