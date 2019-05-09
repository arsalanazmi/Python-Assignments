print("\n")
Name = input("Student's Name = ")
Roll_No = int(input("Student's Roll No. = "))
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
print("------------MARKSHEET------------")
print("\n")
print("SUBJECTS          OBTAINED TOTAL")
print("_________________________________")
print("English         :    "  + str(English)  + "     " + str(100) )
print("Sindhi          :    "  + str(Sindhi)  + "     " +  str(100) )
print("Chemistry       :    "  + str(Chemistry) + "     " +   str(100) )
print("Biology         :    "  + str(Biology)  + "     " +  str(100)  )
print("Pak-Studies     :    "  + str(Pak_Studies) + "     " +  str(100) )
print("_________________________________")
print("Marks Obtained  :  " +  str(Marks_Obtained) + " out of " + str(500))
print("Percentage      :  " +  str(Percentage) + " %")


if (Percentage >= 80) :
    print("Grade           :  A-ONE")
elif (Percentage >= 70 and Percentage < 80) :
    print("Grade           :  A")
elif (Percentage >= 60 and Percentage < 70) :
    print("Grade           :  B")
elif (Percentage >= 50 and Percentage < 60) :
    print("Grade           :  C")
elif (Percentage >= 40 and Percentage < 50) :
    print("Grade           :  D")
else :
    print("Grade           :  Fail")