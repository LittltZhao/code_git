# -*- coding:utf-8 -*-

def searchInsert(nums,target):
    for i in xrange(len(nums)-1):
        if target>nums[i] and target <= nums[i+1]:
            return i+1
s=[1,3,5,6]
print searchIntsert(s,5)
