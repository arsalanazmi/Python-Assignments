# TASK # 08
# TO GET A NEW STRING FROM GIVEN STRING IF IT IS NOT BEGINNING WITH "IS"!

string = input("Enter any String : ")
cons = "is"
if string[:2] == cons:
    print("The given string remains unchanged!" + "\n" + string)
else :
    print("New String:",cons, string) 