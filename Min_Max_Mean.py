import random
arr = []
for rand in range (10) :
    arr.append(random.randint(1,100))
print("List =", arr)

min_value = arr[0]
max_value = arr[0]
sum = 0
for number in arr:
    if min_value > number :
        min_value = number
    elif max_value < number:
        max_value = number
    sum += number
    mean = round( (sum /len(arr)), 2)

print ("Min. value = ",min_value)
print("Index no. of Min. value =", arr.index(min_value))
print ("Max value = ", max_value)
print("Index no. of Max. value =", arr.index(max_value))
print("Mean = Sum / List Length")
print("Sum =", sum)
print("list Length =", len(arr))
print("Mean =", mean)