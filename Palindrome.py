# TASK # 36
# CHECK WHETHER THE GIVEN INPUT IS PALINDFROME OR NOT

pal = input("Enter any Word: ")

if pal == pal[::-1]:
    print("The given input is Palindrome")
else:
    print("The given input is not Palindrome")