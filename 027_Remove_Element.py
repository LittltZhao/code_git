# -*- coding:utf-8 -*-
def removeElement(nums,val):
    i=0
    while i<len(nums):
        if nums[i]==val:
            nums.remove(nums[i])#移除元素后索引依然为原来的值,故要减去1
            i-=1
        i+=1
    return len(nums)
print removeElement([1,13,4,5,1],1)

