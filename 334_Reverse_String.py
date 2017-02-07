# -*- coding:utf-8 -*-
def reverseString(s):
    l=list(s)
    l.reverse()
    return "".join(l)

def reverseString2(s):
    return s[::-1]

def reverseString3(s):
    t=list(s)
    l=len(t)
    for i,j in zip(range(l-1,0,-1),range(l//2)):
        #zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
        t[i],t[j]=t[j],t[i]
    return "".join(t)

print reverseString3('hello')
