# TASK # 30
# COUNT NUMBER OF OCCURENCE OF A SPECIFIC CHARACTER IN A STRING

string = input("ENTER ANY STRING: ")
char = input ("ENTER ANY CHARACTER TO BE COUNT IN A STRING: ")

count = 0
for i in string.lower():
    if i == char.lower():
        count = count + 1
print(count) 