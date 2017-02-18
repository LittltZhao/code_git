# -*- coding:utf-8 -*-

def majorityElement(nums):
    coun=[]
    for i in set(nums):
        coun.append((nums.count(i),i))
    ma=max(coun)
    if ma[0]<len(nums)//2 or len(nums)==0:
        return -1
    return ma[1]

# 由于众数的出现频次大于数据其他所有元素出现频次之和，所以这种对冲抵消最后剩下的一定是众数
def majorityElement2(nums):
    count=1
    n=nums[0]
    for i in range(1,len(nums)):
        if count==0:#选取新的"老大"
            n=nums[i]
            count=1
        else:
            if nums[i]==n:#遇到相同的数加一
                count+=1
            else:#遇到不同的数减去一
                count-=1
    return n
nums=[1,1,1,12,2,2,2,2,2,3,4]
print majorityElement2(nums)

