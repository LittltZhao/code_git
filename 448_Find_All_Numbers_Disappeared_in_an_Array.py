# -*- coding:utf-8 -*-
def findDisappearedNumbers(nums):
    k=range(1,len(nums)+1)
    return list(set(k).difference(set(nums)))#set.difference
    #return set(k)-set(nums)返回类型为set

def findDisappearedNumbers2(nums):
    return list(i for i in range(1,len(nums)+1) if i not in nums)
nums=[1,2,3,4,5,6,7,9]
print findDisappearedNumbers2(nums)
