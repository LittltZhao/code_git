#def factor(n):
#    f=[1]
#    i=2
#    while i<=n:
#        if n%i==0:
#            f.append(i)
#        i+=1
#    return f
#k=factor(100)
#length=len(k)
#if length%2==0:
#    r=[k[length//2-1],k[length//2]]
#else:
#    r=[k[length//2],k[length//2]]
#print r

import math
area=5
val=math.sqrt(area)
if math.modf(val)[0]==0:
    print  [int(val),int(val)]

k=int(val)
i=k
while i<=area:
    if area%i==0:
        if i>val:
            print  [i,area/i]
        else:
            print [area/i,i]
        break
    i+=1

