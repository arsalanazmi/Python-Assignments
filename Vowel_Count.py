# TASK # 34
# COUNT THE OCCURENCE OF VOWELS & CONSONENT IN A TEXT INPUT

text = input("Enter any Text String: ")

count1 = 0
count2 = 0
for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or  i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count1 = count1 + 1
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' and i != ' ':
        count2 = count2 + 1
print("Vowel Count =",count1)
print("Consonent Count =",count2)