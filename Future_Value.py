# TASK # 15
# FUTURE VALUE OF A SPECIFIED PRINCIPAL VALUE, RATE OF INTEREST & NO.OF YEARS

P = int(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
t = int((input("Enter No. Of Years: ")))

r = R/100
A = P *(1+(r*t))

print("Future Value =",A)