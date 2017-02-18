# -*- coding:utf-8 -*-

# 如果有n个台阶，那么走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。所以:
#  f(n) = f(n-1) + f(n-2)。
#  本质为斐波那契数列求解
def climStairs(n):
    dp=[0]*(n+1)
    dp[0]=dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print climStairs(6)
