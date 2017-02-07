# -*- coding:utf-8 -*-
def missingNumber(nums):#等差数列求和减去原来列表的和得到丢失的数据
    i=0
    lens=len(nums)
    sums=0
    while i<lens:
        sums+=nums[i]
        i+=1
    return lens*(lens+1)/2-sums

import operator
def missingNumber2(nums):#与正常的列表进行异或最终得到的就是缺失的数据
    a=reduce(lambda x,y:x^y,nums)#用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果
    b=reduce(operator.xor,range(len(nums)+1))#lambda 函数
    return a^b

print missingNumber2([1,2,3,4,5])
