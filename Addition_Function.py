def sum(a,b,*c):
    sum = a+b
    sum1 = 0
    for i in c:
        sum1 += i
    return sum+sum1
print("Sum =",sum(2,4,6,8,9))