# -*- coding:utf-8 -*-

def isValid(s):
    paren={")":"(","]":"[","}":"{"}
    openpare=["(","[","{"]
    st=[None]
    if len(s)%2:
        return False
    for i in s:
        if i in openpare:
            st.append(i)
        elif paren[i]!=st.pop():
            return False
    return len(st)==1

print isValid('()')

