# -*- coding:utf-8 -*-
def reverse(x):
    sig=1
    if x<0:
        sig=-1
    res=0
    digit=0
    x=abs(x)
    while x:#数字的各个位倒序
        digit=x%10
        x/=10
        res=res*10+digit
    if res>2**31-1:
        return 0
    res*=sig
    return res

def reverse2(x):#转换成字符串进行处理
    x=str(x)
    if x[0]=='-':
        x=-int(str(x[1:])[::-1])
    else:
        x=int(x[::-1])
    if x>2**31-1 or x<-2**31:
        x=0
    return x
print reverse2(1)

        
