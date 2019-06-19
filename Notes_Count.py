# TASK # 35
# FIND THE NUMBER OF NOTES AGAINST A GIVEN AMOUNT

import math
amount = int(input("Enter Any Amount: "))

print("You Will have Notes of 5000 =",math.trunc(amount / 5000))
print("You Will have Notes of 1000 =",math.trunc((amount % 5000) /1000))
print("You Will have Notes of 500 =",math.trunc(((amount % 5000) %1000) /500))
print("You Will have Notes of 100 =",math.trunc((((amount % 5000) %1000) %500) /100)) 
print("You Will have Notes of 50 =",math.trunc(((((amount % 5000) %1000) %500) %100) /50))
print("You Will have Notes of 20 =",math.trunc((((((amount % 5000) %1000) %500) %100) %50) /20))
print("You Will have Notes of 10 =",math.trunc(((((((amount % 5000) %1000) %500) %100) %50) %20) /10))
print("You Will have Coin of 5 =",math.trunc((((((((amount % 5000) %1000) %500) %100) %50) %20) %10) /5))
print("You Will have Coin of 2 =",math.trunc(((((((((amount % 5000) %1000) %500) %100) %50) %20) %10) %5) /2))
print("You Will have Coin of 1 =",math.trunc((((((((((amount % 5000) %1000) %500) %100) %50) %20) %10) %5) %2) /1))