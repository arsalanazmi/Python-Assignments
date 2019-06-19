# TASK # 11
# TO CHECK WHETHER THE GIVEN LETTER IS VOWEL OR NOT

letter = input("Enter any Letter: ")
vowel = ["a","e","i","o","u","A","E","I","O","U"]
for i in vowel: 
    if i == letter:
        print('"' + letter + '" ' + "iS A VOWEL")
        break
else:
    print('"' + letter + '" ' + "iS A CONSONENT")