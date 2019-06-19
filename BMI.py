# TASK # 22
# CALCULATE BODY MASS INDEX

weight = int(input("Enter Your Body Weight in Kg: "))
height = int(input("Enter Height In cm: "))

height = height/100 # cm to m conversion

bmi = round((weight / height**2), 2)
print("Your BMI result =",bmi)

if bmi < 18.5:
    print("You are Underwight")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are Normal Weight")
elif bmi >= 25 and bmi < 29.9:
    print("You are Overweight")
elif bmi >= 30 and bmi < 34.9:
    print("You are Class I Obese")
elif bmi >= 35 and bmi < 39.9:
    print("You are Class II Obese")
elif bmi >= 40:
    print("You are Class III Obese")