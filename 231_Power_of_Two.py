# -*- coding:utf-8 -*-
def isPowerOfTwo(n):
    return n>0 and not (n&(n-1))

print isPowerOfTwo(4)
