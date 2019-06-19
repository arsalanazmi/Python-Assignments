# TASK # 24
# CALCULATE SUM OF THE FIRST N POSITIVE INTEGER NUMBER

n = int(input("ENTER POSITIVE INTEGER NUMBER: "))
sum = 0
for i in range (1,n+1):
    sum += i
print("SUM OF FIRST", n, "INTEGER NUMBER =",sum)