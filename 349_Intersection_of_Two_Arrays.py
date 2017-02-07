# -*- coding:utf-8 -*-
def intersection(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    s=[]
    for i in s1:
        for j in s2:
            if i==j:
                s.append(i)
    return s
def intersection2(nums1,nums2):#列表解析迭代
    return [num for num in set(nums1) if num in nums2]
print intersection2([1,2,2,1],[2,2])


