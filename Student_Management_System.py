Students = []
while True:
    print("\n" + "Student Management System" + "\n")
    print("MAIN MENU"+"\n")
    print('Press 1 to Add Student')
    print('Press 2 to Edit Student')
    print('Press 3 to Search Student')
    print('Press 4 to Delete Student')
    print('Press 5 to Display Student')
    print('Press 6 to Exit')

    choice = int(input("Enter Choice 1-6: "))

    if choice == 1:
        print("Students Addition Menu")
        Student = {}
        Student['Name'] = input('Enter Student Name: ')
        Student['Age'] = int(input('Enter Student Age: '))
        Student['Module'] = input('Enter Student Module: ')
        Students.append(Student)
        print(Student)
        print(Students)
    
    if choice == 2:
        print("Students Edit Menu")
        check = input("Enter Student's Name: ")
        for i in range (len(Students)):
            if Students[i]['Name'] == check:
               Key = input("Enter Key: ")
               for key in Students[i]:
                    if key == Key:
                        Students[i][key] = input("Edit  Student's " + key + ": " )
                        print(Student)
                        print(Students)
                        break
            
    if choice == 3:
        print("Student's Seraching Menu")
        Search = input("Enter Student's Name to be Searched: ")
        for i in range (len(Students)):
            if Students[i]['Name'] == Search:
                print(Students[i]) 
                break

    if choice == 4:
        print("Student's Deletion Menu")
        Delete = input("Enter Student's Name to be Deleted: ")
        for i in range (len(Students)):
            if Students[i]['Name'] == Delete:
                print("Dictionary to be deleted: " + str(Students[i]))
                del Students[i]
                break
        print ("List after deletion of dictionary : " +  str(Students))
    
    if choice == 5:
        print("Student's Display Menu")
        print(Students)

    if choice == 6:
        print("Thanks For Using Student Management System ")
        print("Good Bye")
        break