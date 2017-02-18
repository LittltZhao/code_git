# -*- coding:utf-8 -*-

def isPalindrome(x):#转化为字符串占用了新的空间
    s1=str(x)
    s2=s1[::-1]
    return s1==s2

def isPalindrome2(x):#通用解法
    if x<0:
        return False
    temp=x
    res=0
    while temp:
        res=res*10+temp%10
        temp=temp/10
    return res==x
print isPalindrome2(123201)
