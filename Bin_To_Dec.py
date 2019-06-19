# TASK # 27
# CONVERT BINARY NUMBER INTO DECIMAL NUMBER

binary = input("ENTER A BINARY NUMBER: ")

dec=0
power = len(binary) - 1
for i in binary:
    dec += int(i) * 2 ** power
    power = power - 1
print("DECIMAL EQUVALENT NUMBER = ",dec)  