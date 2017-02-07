# -*- coding:utf-8 -*-
# 列表中如果有相同的数则返回True,否则为False
def containDuplicate(nums):
    sets=set(nums)
    if len(nums)==len(sets):
        return False
    else:
        return True

def containDuplicate2(nums):
    nums.sort()
    for x in range(len(nums)-1):
        if nums[x]==nums[x+1]:
            return True
    return False

def containDuplicate3(nums):
    sets=set()
    for num in nums:
        if num in sets:
            return True
        sets.add(num)
    return False
n=[1,2,3,4,5,6,3,1]
print containDuplicate3(n)


