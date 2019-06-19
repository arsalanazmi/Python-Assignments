# TASK # 33
# PRINT FIRST NAME & LAST NAME IN REVERSE ORDER WITH SPACE B/W THEM 

f_name = input("ENTER FIRST NAME: ")
l_name = input("ENTER LAST NAME: ")

print("FULL NAME IN REVERSED ORDER: ",end="")
for f in reversed(f_name) :
    print(f,end="")
print(end=" ")
for l in reversed(l_name) :
    print(l,end="")