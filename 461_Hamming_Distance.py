def hammingDistance(x,y):
    count=0
    z=x^y
    while z:
        if z%2==1:
            count+=1
        z/=2
    return count

def hammingDistance2(x,y):
    return bin(x^y).count('1')

print hammingDistance2(12,13)
