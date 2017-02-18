# -*- coding:utf-8 -*-
# 字串查找

def strStr(haystack,needle):
    return haystack.find(needle)

def strStr2(haystack,needle):
    nlen=len(needle)
    i=0
    while i<(len(haystack)-len(needle)+1):
        #只需要比较两个字符串长度差次，而不需要比较全部
        j=0
        while j<nlen:
            if haystack[i+j]!=needle[j]:
                i+=1
                break
            j+=1

        if j==nlen:
            return i
        
    return -1

def strStr3(haystack,needle):
    for i in xrange(len(haystack)-len(haystack)+1):
        if haystack[i:i+len(needle)]==needle:#切片
            return i
    return -1

s1="abcdegf"
s2="bcd"
print strStr2(s1,s2)
