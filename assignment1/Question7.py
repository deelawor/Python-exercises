while True:
    med_list = ["Panadol", "Dolipran", "Fervex", "Spasfon", "Gastrogel", "Amoxyl"]
    print("Tasks: 1.Add an item to stock pharmacy, 2.Remove item from stock or 3.Insert item at specified position.")
    task = int(input("Choose task by typing '1' to add, '2' to remove or '3' to insert at specific position."))
    if task == 1:
        newMed = input("Enter name of the medecine: ").title()
        med_list.append(newMed)

    elif task == 2:
        reMed = input("Enter name of medecine to be removed: ").title()
        med_list.remove(reMed)
    elif task == 3:
        newMed = input("Enter name of medecine to be added: ")
        position = int(input("At which position should this medecine be placed? "))
        med_list.insert((position - 1), newMed)
    else:
        print("The task you entered is invalid. please choose again.")

    print(med_list)
    x = input("Do you need to do another task again? ").lower()
    if x == "yes":
        continue
    else:
        break










