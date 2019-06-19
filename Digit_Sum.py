# TASK # 25
# CALCULATE SUM OF THE DIGITS IN AN INTEGER

n = input("ENTER POSITIVE INTEGER NUMBER: ")
sum = 0
for i in n:
    sum += int(i)  
print("SUM OF GIVEN DIGITS",n,"=",sum)
 