# TASK # 41

n = int(input("Enter no. of rows: "))
for i in range (0,n):
    for j in range (0,i):
        print("*",end="")
    print("\r")

for i in reversed(range(0,n+1)):
    for j in range(0,i):
        print("*",end="")
    print("\r")

# TASK # 42

n = int(input("Enter no. of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("\r")

for i in reversed(range(1,n+1)):
    for j in range(1,i):
        print(j,end="")
    print("\r")

# TASK # 43

n =  int(input("Enter no. of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")