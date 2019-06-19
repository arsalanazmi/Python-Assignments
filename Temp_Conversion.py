# TASK # 23
# TEMPERATURE CONVERSION TO & FROM CELCIUS, FAHRENHEIT

temp = float(input("ENTER TEMPERATURE TO CONVERT: "))
deg = input("ENTER DEGREE 'F' FOR FAHRENHEIT 'C' FOR CELCIUS: ")

if deg == "c" or deg == "C":
    cel = round( ( (temp - 32) * (5/9) ), 2) 
    print("TEMPERATURE IN CELCIUS =",cel,"°C")
elif deg == "f" or deg =="F":
    far = round( ( temp * (9/5) + 32 ), 2)
    print("TEMPERATURE IN FAHRENHEIT =",far,"°F")