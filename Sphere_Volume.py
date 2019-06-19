# TASK # 06
# CALCULATE VOLUME OF SPHERE BY TAKING RADIUS FROM USER

import math
radius = float(input("Radius of Sphere = "))
volume = round( (4/3) * math.pi * radius**3, 2)
print("Volume of Sphere = 4/3 πr^3 =",volume)