# -*- coding:utf-8 -*-

def merge(nums1,m,nums2,n):
    i=0
    if nums1[0]>nums2[-1]:
        nums2.extend(nums1)
        nums1=nums2
    elif nums1[-1]<nums[0]:
        nums1.extend(nums2)
    while i<len(nums1):
        j=0

