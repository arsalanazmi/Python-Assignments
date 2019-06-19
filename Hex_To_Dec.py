# TASK # 29
# CONVERSION OF HEXADECIMAL NUMBER INTO DECIMAL NUMBER

hex = input("ENTER A HEXADECIMAL NUMBER: ")

dec = 0
power = len(hex) - 1

for i in range(len(hex)):
    if hex[i] == "A":
        dec = dec + 10*16**power   
    elif hex[i] == "B":
        dec = dec + 11*16**power   
    elif hex[i] == "C":
        dec = dec + 12*16**power    
    elif hex[i] == "D":
        dec = dec + 13*16**power
    elif hex[i] == "E":
        dec = dec + 14*16**power
    elif hex[i] == "F":
        dec = dec + 15*16**power
    else : 
        dec = dec + int(hex[i]) * 16 ** power
    power = power - 1

print("DECIMAL EQIVALENT NUMBER =",dec)