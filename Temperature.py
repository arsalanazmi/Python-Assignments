temp = int(input("Enter Temperature in °C : "))

if temp <= 0 :
    print("Its", temp, "°C ~ Too Cold")
    print("Turn on Heater")
elif temp > 0 and temp <= 22 :
   print("Its", temp, "°C ~ Good Weather")
   print("Turn off the fan")
elif temp > 22 and temp <=35 :
   print("Its", temp, "°C ~ Sunny Weather")
   print("Turn on the fan")
else:
   print("Its", temp, "°C ~ Hot Weather")
   print("Turn on the A.c")
