l=[1,1,0,1,1,1]
def findMaxConsecutiveOnes(nums):
    k=0
    count=[]
    for i in l:
        if i==1:
            k+=1
        elif i==0:
            count.append(k)
            k=0
    count.append(k)
    return max(count)
l=[1,1,0,1,1,1]
print findMaxConsecutiveOnes(l)

