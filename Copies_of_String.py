# TASK # 09
# GET STRING WHICH IS N (NUMBER OF COPIES) OF GIVEN STRING:

string = input("Enter any String: ")
n = int(input("Enter a Non-Negative Integer: "))
copies = (string + "\n" ) * n
print(copies)