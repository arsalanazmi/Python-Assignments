# TASK # 05

# NO. OF DAYS B/W CURRENT AND GIVEN DATE
import datetime

Current_Date = datetime.datetime.now()
Previous_Date = datetime.datetime(1992, 3, 8, 23,27,45,198765)

print("CURRENT DATE :", Current_Date)
print("MY BIRTH DATE :", Previous_Date)

No_Of_Days = Current_Date - Previous_Date 
print("I AM", No_Of_Days.days, "DAYS OLD")
print("\n************************************\n")


# NO. OF DAYS B/W TWO USER DEFINED DATES 
from datetime import date

print("WRITE THE DATE IN THIS  FORMAT: DD-MM-YYYY")
d1,m1,y1 = (input("ENTER  FIRST DATE: ")).split("-")
d2,m2,y2 = (input("ENTER SECOND DATE: ")).split('-')

d1 = int(d1)
m1 = int(m1)
y1 = int(y1)
d2 = int(d2)
m2 = int(m2)
y2 = int(y2)

date1= date(y1,m1,d1)
date2 = date(y2,m2,d2)

period = abs(date1-date2)
print("DAYS BETWEEN TWO DATES IS:",period.days)