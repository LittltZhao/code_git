# -*- coding:utf-8 -*-
# 字符串中第一个不重复字母的索引
def check(s):
    have_done=[]
    for i in range(0,len(s)):
        if s[i] not in have_done:
            if s.count(s[i])==1:
                return i
            else:
                have_done.append(s[i])
        else:
            continue
    return -1
print check("leetcode")

