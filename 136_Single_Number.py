# -*- coding:utf-8 -*-
def singleNumber(nums):
    res=0
    for i in range(len(nums)):
        res^=nums[i]
    return res


def singleNumber2(nums):
    nums.sort()
    for i in range(1,len(nums),2):
        if nums[i]!=nums[i-1]:
            return nums[i-1]
    return nums[-1]
print singleNumber2([1,2,2,4,5,6,6,5,4])
