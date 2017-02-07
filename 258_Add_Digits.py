# -*- coding:utf-8 -*-

def addDigits(num): 
    l=[]
    while True:
        while num!=0:
            l.append(num%10)
            num/=10
        s=sum(l)
        if s/10==0:
            return s
        num=s
def addDigits2(num):#每9个一循环，所有大于9的数的树根都是对9取余，那么对于等于9的数对9取余就是0了，为了得到其本身，而且同样也要对大于9的数适用，我们就用(n-1)%9+1这个表达式来包括所有的情况
    return (num-1)%9+1


print addDigits2(17)
