# -*- coding:utf-8 -*-

def reverseBits(n):#方法一
    count=32
    num=0
    i=0
    while i<count:
        if n%2==1:
            num+=2**(count-i-1)
        n/=2
        i+=1
    return num

def reverseBits1(n):#bin()将数字转化为二进制字符串
    b=bin(n)[:1:-1]
    print b
    return int(b+'0'*(32-len(b)),2)#int(n,2)表示将2进制所表示的n转换为int型


def reverseBits2(n):#位操作
    res=0
    for i in xrange(32):
        res<<=1#左移表示乘以2
        res|=((n>>i)&1)#右移表示处以2
    return res
def reverseBits3(n):#每次处理一半的位交换
    n=(n>>16)|(n<<16)
    n=((n&0xff00ff00)>>8)|((n&0x00ff00ff)<<8)
    n=((n&0xf0f0f0f0)>>4)|((n&0x0f0f0f0f)<<4)
    n=((n&0xcccccccc)>>2)|((n&0x33333333)<<2)
    n=((n&0xaaaaaaaa)>>1)|((n&0x55555555)<<1)
    return n

print reverseBits3(43261596)


# s='abcdef' 字符串切片
# print s[1:]
# print s[:1]
# print s[:1:-1] 
