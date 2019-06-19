# TASK # 31
# COMPUTE THE GCD OF TWO POSITIVE INTEGERS

num1 = int(input("ENTER INTEGER 1: "))
num2 = int(input("ENTER INTEGER 2: "))

i = 1
while (i <= num1 and i <= num2):
    if ((num1 % i) == 0 and (num2 % i) == 0) :
        gcd = i
    i = i + 1
print("THE GCD OF {0} & {1} = {2}".format(num1,num2,gcd))
