# TASK # 19
# CONVERT DISTANCE IN FEET TO INCHES YARDS & MILES

feet = int(input("Enter Distance in Feet: "))
inches = feet * 12
yards = round( (feet /3) ,2)
miles = round( (feet /5280), 4)
print("Distance in Inches:",inches)
print("Distance in Yards:",yards)
print("Distance in Miles:",miles)