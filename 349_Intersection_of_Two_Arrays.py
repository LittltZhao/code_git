# -*- coding:utf-8 -*-
def solution(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    s=[]
    for i in s1:
        for j in s2:
            if i==j:
                s.append(i)
    return s

# print solution([1,2,2,1],[2,2])


