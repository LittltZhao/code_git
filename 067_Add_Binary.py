# -*- coding:utf-8 -*-
def addBinary(a,b):
    bin1=int(a,2)
    bin2=int(b,2)
    c=bin1+bin2
    return bin(c)[2:]#bin()返回二进制字符串且前面多类0b表示二进制


# 从两个字符串的最低位开始，一位一位的进行二进制相加，并保存进位，最终可以得到两者的和的字符串
def addBinary2(a,b):
    res=''
    i,j,plus=len(a)-1,len(b)-1,0
    while i>=0 or j>=0 or plus==1:
        plus+=int(a[i]) if i>=0 else 0
        plus+=int(b[j]) if j>=0 else 0
        res=str(plus%2)+res
        i,j,plus=i-1,j-1,plus/2
    return res

s1='100'
s2='1'
print addBinary2(s1,s2)
