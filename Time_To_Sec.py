# TASK # 20
# CONVERT ALL UNITS OF TIME INTO SECENDS

years = int(input("Enter Time In No. of Years: "))
months = int(input("Enter Time In No. of Month: "))
weeks = int(input("Enter Time In No. of Weeks: "))
days = int(input("Enter Time In No. of Days: "))
hours = int(input("Enter Time In No. of Hours: "))
mins = int(input("Enter Time In No. of Mins: "))

y = years * 365.25 * 24 * 60 * 60  
print("Years To Second Conversion: ",y)
mo = months * 30 * 24 * 60 * 60  
print("Months To Second Conversion: ",mo)
w = weeks * 7 * 24 * 60 * 60  
print("Weeks To Second Conversion: ",w)
d = days * 24 * 60 * 60  
print("Days To Second Conversion: ",d)
h = hours * 60 * 60  
print("Hours To Second Conversion: ",h)
mi = mins * 60
print("Minutes To Second Conversion: ",mi)