# TASK # 13
# RETURN TRUE IF TWO GIVEN NUMBERS ARE EQUAL OR THIER SUM OR DIFFERENCE IS 5

number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second Number: "))

if number1 == number2:
    print("Two Numbers are Equal" + "\n" +"True")
elif (number1 + number2) == 5:
    print("Sum of Two Numbers is: 5" + "\n" + "True")
elif abs(number1 - number2) == 5:
    print("Difference of Two Numbers is: 5" + "\n" + "True")
else :
    print("False")