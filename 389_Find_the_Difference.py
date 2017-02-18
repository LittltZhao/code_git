# -*- coding:utf-8 -*-

import operator
def findTheDifference(s,t):#异或
    return chr(reduce(operator.xor,map(ord,s+t)))
#map()第一个参数接收一个函数名，第二个参数接收一个可迭代对象


def findTheDifference2(s,t):
    count=[0]*26
    for i in s:
        count[ord(i)-97]+=1
    for i in t:
        count[ord(i)-97]-=1
        if count[ord(i)-97]<0:
            return i
s="abcd"
t="abcdk"
print findTheDifference2(s,t)
