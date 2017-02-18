# -*- coding:utf-8 -*-
def intersect(nums1,nums2):
    k=[]
    for i in nums1:
        index=-1
        for j in xrange(0,len(nums2)):
            if nums2[j]==i:
                index=j
                break
        if index != -1:
            k.append(i)
            del nums2[index]#删除避免多次匹配
    return k

#用字典统计第一个列表都出现了哪些数及出现的次数，然后顺序遍历第二个列表，发现同时出现的数则加入到结果列表中，同时将第一个列表中相应的出现次数减一。
def intersect2(nums1,nums2):
    res=[]
    maps={}
    for i in nums1:
        maps[i]=maps[i]+1 if i in maps else 1
    for j in nums2:
        if j in maps and maps[j]>0:
            res.append(j)
            maps[j]-=1#避免多次匹配
    return res

nums1=[1,2,2,4]
nums2=[2,2]
print intersect2(nums1,nums2)
