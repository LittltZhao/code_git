# -*- coding:utf-8 -*-

def mySqrt(x):#折半查找
    if x==0:
        return 0
    i,j=1,x/2+1
    while i<=j:
        center=(i+j)/2
        if center**2==x:
            return center
        elif center**2<x:
            j=center-1
        else:
            i=center+1
    return j#循环结束后必然有i>=j，故返回j
print mySqrt(1)

