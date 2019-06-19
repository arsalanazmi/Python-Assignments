# PRIME NO. TABLE FROM (1-100)
print("\nPrime no. table from 1 to 100 \n")
for val in range (1,101) :
    if val > 1 :
        for num in range(2,val):
            if (val % num) == 0:
                break
        else :
            print(val)
print("********************************\n")

# PRIME NO. CHECKER
print("Prime No. Checker \n")
number = int(input("Enter any number: "))
if number > 1 :
    for i in range (2, number) :
        if (number % i) == 0 :
            print("\n", number, "is not a prime number.")
            break
    else :
        print("\n", number, "is a prime number.")
# If entered no. is less than or equal to 1 then it is not a prime no.
else :
    print("\n", number, "is not a prime number.")