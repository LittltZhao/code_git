# -*- coding:utf-8 -*-
#给定数组和特定的数组，使数组中两个数相加等于给定的数
def twoSum(nums,target):
    lens=len(nums)
    nums1=nums[:]
    index=[]
    nums.sort()
    i,j=0,lens-1
    while i<j:
        if nums[i]+nums[j]==target:
            for k in range(0,lens):
                if nums1[k]==nums[i]:
                    index.append(k)
            for k in range(lens-1,-1,-1):
                if nums1[k]==nums[j]:
                    index.append(k)
            return [index[0],index[1]]
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            i+=1
nums=[2,7,11,15]
print twoSum(nums,9)
