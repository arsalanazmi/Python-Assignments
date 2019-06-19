# TASK # 21
# CONVERT SECONDS TO DAYS, HOURS & MINUTES

sec = int(input("Enter no. of Seconds: "))

# 1 day = 86400 sec.
days = sec / (60*60*24)
print("Seconds To Days Conversion: ",days)

# 1 Hour = 3600 Sec.
hours = sec / (60*60)
print("Seconds To Hours Conversion: ",hours)

# 1 min = 60 sec
mins = sec / (60)
print("Seconds To Minutes Conversion: ",mins)