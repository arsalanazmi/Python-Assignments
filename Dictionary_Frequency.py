# Determine Frequency of a Dictionary Using Function
def freq(list):
    freq_table = {}
    for i in list:
        if i in freq_table:
            freq_table[i] += 1
        else:
            freq_table[i] = 1
    return freq_table

print(freq(["Apple","Apple",'Grapes',"banana","Grapes"]))


# Determine Frequency of a Dictionary from User Input List Items
List = []
n = int(input("Enter no. of Fruits to be added in the list: "))
for i in range(0,n):
    fruits = input("Enter Fruit: ")
    List.append(fruits)
print("List of Fruits:",List)

freq = {}
for i in List:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1    
print("Frequency of Fruits:",freq)