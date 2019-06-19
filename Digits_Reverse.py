# TASK # 37
# REVERSE THE DIGITS OF A GIVEN NO AND ADD IT TO THE ORIGINAL, IF THE SUM IS NOT IS PALINDRPME REPEAT THE PROGRAM:

number = int(input("Enter any Number: "))

while True:
    num = str(number)
    if num == num[::-1]:
        print("The Number",number,"is a Palidrome")
        break
    else:
        reverse_number = int(num[::-1])
        number += reverse_number
        print(number)