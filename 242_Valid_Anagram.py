# -*- coding:utf-8 -*-
def isAnagram(s,t):
    return sorted(s)==sorted(t)#sort是在原位重新排列列表，而sorted()是产生一个新的列表。

def isAnagram2(s,t):#统计每个字符出现的次数并进行判断
    if len(s)!=len(t):
        return False
    alpha=[0]*26
    beta=[0]*26
    for c in s:
        alpha[ord(c)-97]+=1
    for c in t:
        beta[ord(c)-97]+=1
    return alpha==beat

def isAnagram2(s,t):#unicode码适用
    if len(s)!=len(t):
        return False
    alpha={}
    beta={}
    for c in s:
        alpha[c]=alpha.get(c,0)+1#get(key,0)返回key对应的键值，不存在则返回0
    for c in t:
        beta[c]=beta.get(c,0)+1
    return alpha==beta
