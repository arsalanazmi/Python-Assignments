# User Input List
List=[]
n = int(input("Enter no. of items to be added in a List: "))
for i in range(0,n):
    list = int(input("Enter any no.: "))
    List.append(list)
print("List:",List)

# FUNCTION FOR CALCULATING LIST LENGTH 
def length(list):
    count = 0
    for i in list:
        count += 1
    return count
print("Length of List is:",length(List))

# FUNCTION FOR CALCULATING LIST SUM
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print("Sum of List is:",sum(List))

# FUNCTION FOR CALCULATING LIST AVERAGE
def avg(list):
    avg = sum(List)/length(List)
    return avg
print("Average of List is:", avg(List))