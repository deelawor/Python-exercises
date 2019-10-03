while True:
    li_one = []
    li_two = []
    li_three = []
    print("Your first list: ")
    num = int(input("How many numbers will you put in the list? "))
    for n in range(num):
        numbers = int(input("Enter number: "))
        li_one.append(numbers)
    for i in li_one:
        if i % 2 != 0:
            li_three.append(i)

    print("Your second list: ")
    num = int(input("How many numbers will you put in the list? "))
    for n in range(num):
        numbers = int(input("Enter number: "))
        li_two.append(numbers)
    for i in li_two:
        if i % 2 == 0:
            li_three.append(i)

    print("Your first list is ", li_one)
    print("Your second list is ", li_two)
    print("The third list is ", li_three)

    x = input("Do you wish to retry? ").lower()
    if x == "yes":
        continue
    else:
        break
