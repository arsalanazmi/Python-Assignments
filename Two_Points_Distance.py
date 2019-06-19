# TASK # 16
# COMPUTE DISTANCE B/W TWO POINTS

import math

x1 = int(input("Enter Value x1: "))
y1 = int(input("Enter Value y1: "))
x2 = int(input("Enter Value x2: "))
y2 = int(input("Enter Value y2: "))

distance = round( math.sqrt( math.pow( (x2-x1), 2) + math.pow( (y2-y1), 2) ), 2)
print("DISTANCE BETWEEN TWO POINTS IS:", distance)