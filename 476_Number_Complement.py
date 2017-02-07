# -*- coding:utf-8 -*-

def findComplement(num):
    mask,temp=1,num
    while temp>0:#通过while循环得到num转换为二进制的位数
        mask<<=1
        temp>>=1
    return num^(mask-1)#与1进行异或求反

print findComplement(5)
