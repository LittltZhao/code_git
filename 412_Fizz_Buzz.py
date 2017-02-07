def fizzBuzz(n):
    ls=[0]*n
    for i in range(len(ls)):
        if (i+1)%15==0:
            ls[i]='FizzBuzz'
        elif (i+1)%5==0:
            ls[i]='Buzz'
        elif (i+1)%3==0:
            ls[i]='Fizz'
        else:
            ls[i]=str(i+1)
    return ls

print fizzBuzz(15)

