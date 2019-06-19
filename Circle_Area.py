# TASK # 01
# COMPUTE THE AREA OF CIRCLE BY TAKING RADIUS BY USER

import math
radius = float(input("Enter Radius of Circle: "))
area = round(math.pi * radius**2,2)
print("Area of Circle = πr2 =", area)