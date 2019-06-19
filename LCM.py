# TASK # 32
# FIND THE LCM OF TWO POSITIVE NUMBERS

num1 = int(input("ENTER INTEGER 1: "))
num2 = int(input("ENTER INTEGER 2: "))

if (num1 > num2):
    maximum = num1
else :
    maximum = num2

while (True):
    if (maximum % num1) == 0 and (maximum % num2) == 0:
        print("THE LCM OF {0} and {1} = {2}" .format(num1,num2,maximum) )
        break
    maximum = maximum + 1