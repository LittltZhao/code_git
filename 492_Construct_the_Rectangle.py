import math
def constructRectangle(area):
    val=math.sqrt(area)
    if math.modf(val)[0]==0:
        print  [int(val),int(val)]
    i=int(val)
    while i<=area:
        if area%i==0:
            if i>val:
                print  [i,area/i]
            else:
                print [area/i,i]
            break
        i+=1

def constructRectangle2(area):
    val=int(math.sqrt(area))
    L,W=area,1
    for x in range(val,0,-1):
        if area%x==0:
            L,W=area/x,x
            break
    return [L,W]
print constructRectangle2(20)
