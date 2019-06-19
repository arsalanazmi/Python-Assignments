# TASK # 03
# TO CHECK WHETHER A NUMBER IS COMPLETLY DIVISIBLE BY ANOTHER NUMBER OR NOT

number1 = int(input("Enter first number: "))
number2 = int(input("Enter Second number: "))

print("Remainder = ",number1,"%", number2,"=",number1 % number2)
if (number1 % number2) == 0 :
    print(number1,"is completly divisible by",number2)
else :
    print(number1,"is not completly divisible by",number2)