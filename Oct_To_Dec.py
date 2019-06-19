# TASK # 28
# CONVERSION OF OCTAL NUMBER INTO DECIMAL NUMBER

octal = input("ENTER A OCTAL NUMBER: ")

dec = 0
power = len(octal) - 1
for i in octal:
    dec += int(i) * 8 ** power
    power = power - 1
print("DECIMAL EQUIVALENT NUMBER =",dec)