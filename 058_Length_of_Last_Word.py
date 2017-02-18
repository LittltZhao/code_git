# -*- coding:utf-8 -*-
def lengthofLastWord(s):
    n= s.split()
    if not n:#列表为空的判断
        return 0
    else:
        return len(n[-1])

def lengthofLastWord2(s):
    return s.rstrip()
    return len(s.rstrip().split(' ')[-1])#rstrip()删除末尾指定字符串

#先删除末尾的空格之后再统计末尾字符个数，直到遇到' '停止
def lengthofLastWord3(s):
    length,j=0,len(s)-1
    while j>=0:
        if s[j]!=' ':
            break
        j-=1
    for i in xrange(j,-1,-1):
        if s[i]==' ':
            return length
        length+=1
    return length



print lengthofLastWord('')
