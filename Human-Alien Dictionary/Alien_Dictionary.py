import json
import Dictionary
while True:
    print("\n\n===== HUMAN (ENGLISH) / ALIEN  DICTIONARY =====")
    print ("\n\t\t  MAIN MENU\n")
    print("SELECT ANY 1 OPTION")
    print("Press [1] for Alien to Human (English) Dictionary")
    print("Press [2] for Human (English) to Alien Dictioanry")
    print("Press [3] to Add new word to Alien to Human (English) Dictionary")
    print("Press [4] to Add new word to Human (English) to Alien Dictionary")
    print("Press [5] to Edit Human (English) Translation of Alien language Word")
    print("Press [6] to Edit Alien Translation of Human (English) language Word")
    print("Press [7] to Display Alien to Human (English) Dictionary")
    print("Press [8] to Display Human (English) to Alien Dictionary")
    print("Press [9] to Exit")

    choice = int(input("Enter your Choice [1/9]: "))

    try:
        with open("Alien_Dictionary.json") as f:
            dictionary = json.load(f)

        if choice == 1:
            print("\nAlien To Human (English) Dictionary \n")
            alien = input("Enter any word of Alien language : ")

            for k,v in dictionary.items():
                if alien.title() == k:
                    print("Alien phrase = " + k + "\nHuman (English) Translation = " + v + "\n")
                    break
            else:
                print('Word "' + alien + '" not found in Alien Dictionary \n')
                    
        elif choice == 2:
            print("\nHuman (English) To Alien Dictionary \n")
            English = input("Enter any word of Human (English) language: ")
            
            for k,v in dictionary.items():
                if English.title() == v:
                    print("Human (English) Phrase =",v,"\nAlien Translation =",k,"\n")
                    break
            else:
                print('Word "' + English + '" not found in Human (English) Dictionary \n')                

        elif choice == 3:
            print("\nAdd New Word In Alien Dictionary\n")
            alien = input("Enter new word of Alien language: ")
            human = input("Enter meaning of the word in Human (English) language: ")
            alien = alien.title()
            human = human.title() 
            Dictionary.Alien_Dictionary.update({alien:human})
            Dictionary.write_to_json()

        elif choice == 4:
            print("\nAdd New Word In Human (English) Dictionary\n")
            human = input("Enter word of Human (English) language: ")
            alien = input("Enter meaning of the word in Alien language: ")
            human = human.title()
            alien = alien.title() 
            Dictionary.Alien_Dictionary.update({human:alien})
            Dictionary.write_to_json()
                
        elif choice == 5:
            alien = input("\nEnter Alien language word whose meaning you want to edit: ")
            for k,v in dictionary.items():
                if k == alien.title():
                    human = input("Edit Meaning: ")
                    human = human.title()
                    alien = alien.title()
                    Dictionary.Alien_Dictionary.update({alien:human})
                    Dictionary.write_to_json()
                    break
            else:
                print("Word '" + alien + "' doesn't exist in Alien to Human (English) Dictionary")       

        elif choice == 6:
            human = input("\nEnter Human (English) language word whose meaning you want to edit: ")
            for k,v in dictionary.items():
                if human.title() == v:
                    alien = input("Edit Meaning: ")
                    alien = alien.title()
                    human = human.title()
                    del Dictionary.Alien_Dictionary[k]
                    Dictionary.Alien_Dictionary.update({alien:human})
                    Dictionary.write_to_json()
                    break
            else:
                print("Word '" + human + "' doesn't exist in Human (English) to Alien Dictionary") 

        elif choice == 7:
            print("\nDisaplay Alien To Human (English) Dictionary\n")
            print("Alien\t\t:\tEnglish")
            
            x = ' '
            space = 0
            for k,v in dictionary.items():
                for i in k:
                    space = 16-len(k)
                    print(k + (x*space) +":\t"+v)  
                    break                

        elif choice == 8:
            print("\nDisplay Human (English) To Alien Dictionary\n")
            print("English\t\t:\tAlien")

            x = ' '
            space = 0
            for k,v in dictionary.items():
                for i in v:
                    space = 16 - len(v)
                    print(v + (x*space) + ":\t" + k)
                    break

        elif choice == 9:
            print("\nDo you really want to Exit ?")
            exit = input("Press [Y] for Yes [N] for No: ")

            if exit.lower() == 'y':
                print("Thanks for using Human/Alien Dictionary")
                print("Good Bye")
                break
            elif exit.lower() == 'n':
                continue
            while True:
                if exit.lower() != 'n':
                    exit = input("Press [Y] for Yes [N] for No: ")   
                    if exit.lower() == 'y':
                        print("Thanks for using Human/Alien Dictionary")
                        print("Good Bye")
                        break
                    else:
                        continue
                break
            if exit.lower() == 'y':
                break  

    except FileNotFoundError:
        print("\nSorry, File Not Found !")
        Dictionary.write_to_json()
        print("New Dictionary Created!\nTry Again !")