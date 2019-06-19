# TASK # 26
# CONVERT DECIMAL NUMBER TO BINARY, OCTAL & HEXADECIMAL NUMBERS

decimal = int(input("ENTER A DECIMAL NUMBER: "))

# BINARY CONVERSION
binary = ""
while decimal > 0:
        rem = decimal % 2
        decimal = decimal // 2
        binary = str(rem) + binary
print("BINARY NUMBER CONVERSION =",binary)

# OCTAL CONVERSION
decimal = int(input("ENTER A DECIMAL NUMBER: "))
octal = ""
while decimal > 0:
        rem = decimal % 8
        decimal = decimal // 8
        octal = str(rem) + octal
print("OCTAL NUMBER CONVERSION =",octal)

# HEXADECIMAL CONVERSION
decimal = int(input("ENTER A DECIMAL NUMBER: "))
lst = '0123456789ABCDEF'
hexadecimal = ""
while decimal > 0:
        rem = decimal % 16
        decimal = decimal // 16
        hexadecimal = str(lst[rem]) + hexadecimal
print("HEXADECIMAL NUMBER COVERSION =",hexadecimal)