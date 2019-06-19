# TASK # 17
# CONVERT HEIGHT (IN FEET & INCHES) TO CENTIMETERS

h_feet = int(input("Enter Height in feet: "))
h_inches = int(input("Enter height in inches: "))

h_centi1 = h_feet * 30.48
h_centi2 = h_inches * 2.54
  
print("Total Height (feet & inches): ",h_feet, "feet &", h_inches, "inches")
print("Total Height in cm: ",h_centi1+h_centi2)