def add(x,y) :
    return x + y

def sub(x,y) :
    return x - y

def mul(x,y) :
    number = x * y
    number = round(number,2)
    return number

def div(x,y) :
    number = round((x/y),2)
    return number

print("\n")
print ("Select opertion to perform \n")
print ("Press '1' for Addition")
print ("Press '2' for Subtraction")
print ("Press '3' for Multiplication")
print ("Press '4' for Division \n")

choice = int(input("Enter choice for action to perform (1/2/3/4) : "))

number1 = float(input("\nEnter Operand 1 : "))
number2 = float(input("Enter Operand 2 : "))

if choice == 1 :
    print ("\n",number1, "+", number2, "=", add(number1, number2))

elif choice == 2 :
    print ("\n",number1, "-", number2, "=", sub(number1, number2))

elif choice == 3 :
    print ("\n",number1, "*", number2, "=",  mul(number1, number2))

elif choice == 4 :
    print ("\n",number1, "/", number2, "=", div(number1, number2))

else :
    print ("\nInvalid Input")