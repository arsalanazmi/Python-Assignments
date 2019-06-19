# TASK # 18
# CALCULATE HYPOTENUSE OF RIGHT ANGLED TRIANGLE

import math
base = int(input("ENTER BASE OF RIGHT ANGLED TRIANGLE: "))
height = int(input("ENTER HEIGHT OF RIGHT ANGLED TRIANGLE: "))

hypotenuse = round(math.sqrt(base**2 + height**2),2)
print("Hypotenuse of Right Angled Triangle =",hypotenuse)