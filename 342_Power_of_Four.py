# -*- coding:utf-8 -*-
#判断一个数是否为4的幂数
def isPowerOfFour(num):
    return num>0 and (num&(num-1))==0 and (num-1)%3==0#(num&(num-1))==0判断是否为2的幂

print isPowerOfFour(16)
