# -*- coding:utf-8 -*-
# 数字转化为二进制后含有1的个数
def hammingWeight(n):
    count=0
    while n!=0:
        if n%2==1:
            count+=1
        n/=2
    return count

def hammingWeight2(n):#移位操作
    count=0
    while n:
        count+=n&1
        n>>=1

def hammingWeight3(n):
    return bin(n).count('1')

def hammingWeight4(n):#运算n = n&(n-1)可以将n最低位的1变成0.循环进行该运算，循环次数就是n的二进制表示中1的个数。
    count=0
    while n:
        count+=1
        n&=n-1
    return count
print hammingWeight(11)
