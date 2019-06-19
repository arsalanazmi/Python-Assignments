# TASK # 40
# CALCULATE THE NUMBER OF LETTERS & DIGITS FROM A GIVEN STRING 

string = input("Enter any string: ")

letter_count = 0
digit_count = 0

for i in string: 
    for j in range (65,91):
        if i == chr(j):
            letter_count += 1
    for k in range (97,123):
        if i == chr(k):
            letter_count += 1
    for l in range (48,58):
        if i == chr(l):
            digit_count += 1

print("Number of Letters in given String:",letter_count)
print("Number of Digits in given String:",digit_count)