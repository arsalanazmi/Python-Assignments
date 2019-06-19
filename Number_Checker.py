# TASK # 02
# TO CHECK WHETHER THE USER GIVEN NUMBER IS POSITIVE, NEGATIVE OR ZERO

number = int(input("Enter a number to check: "))

if number < 0:
    print("The given number",number, "is Negative")
elif number == 0:
    print("The given number",number, "is Zero")
else:
    print("The given number",number, "is Positive")