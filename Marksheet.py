print("\n")
Name = input("Student's Name = ")
Roll_No = int(input("Student's Roll No. = "))
School_Name = input("School Name = ")
print("\n")

English = int(input("Marks of English = "))
Sindhi = int(input("Marks of Sindhi = "))
Chemistry = int(input("Marks of Chemistry = "))
Biology = int(input("Marks of Biology = "))
Pak_Studies = int(input("Marks of Pak-Studies = "))

Total_Marks = 500
Marks_Obtained = English + Sindhi + Chemistry + Biology + Pak_Studies
Percentage = round(((Marks_Obtained/Total_Marks) * 100),2)

print("\n")
print("-------------MARKSHEET-------------")
print("\n")
print("SUBJECTS \t   OBTAINED   MAX.")
print("___________________________________")
print("English\t\t :    " + str(English) + "      " + str(100) )
print("Sindhi\t\t :    "  + str(Sindhi)  + "      " +  str(100) )
print("Chemistry\t :    "  + str(Chemistry) + "      " +   str(100) )
print("Biology\t\t :    "  + str(Biology)  + "      " +  str(100)  )
print("Pak-Studies\t :    "  + str(Pak_Studies) + "      " +  str(100) )
print("___________________________________")
print("TOTAL\t\t :    " +  str(Marks_Obtained) + "     " + str(Total_Marks))
print("PERCENTAGE\t :    " +  str(Percentage) + " %")


if (Percentage >= 80) :
    print("GRADE\t\t :    A-ONE")
elif (Percentage >= 70 and Percentage < 80) :
    print("GRADE\t\t :    A")
elif (Percentage >= 60 and Percentage < 70) :
    print("GRADE\t\t :    B")
elif (Percentage >= 50 and Percentage < 60) :
    print("GRADE\t\t :    C")
elif (Percentage >= 40 and Percentage < 50) :
    print("GRADE\t\t :    D")
else :
    print("GRADE\t\t :    Fail")