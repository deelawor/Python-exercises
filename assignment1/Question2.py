while True:
    li_one = []
    li_two = []
    li_three = []
    li_four = []
    li_sum = []

    print("List1: ")
    for n in range(4):
        numbers = int(input("Enter number"))
        li_one.append(numbers)

    print("List2: ")
    for n in range(4):
        numbers = int(input("Enter number"))
        li_two.append(numbers)

    print("List3: ")
    for n in range(4):
        numbers = int(input("Enter number"))
        li_three.append(numbers)

    print("List4: ")
    for n in range(4):
        numbers = int(input("Enter number"))
        li_four.append(numbers)

    one = sum(li_one)
    two = sum(li_two)
    three = sum(li_three)
    four = sum(li_four)

    li_sum.append(one)
    li_sum.append(two)
    li_sum.append(three)
    li_sum.append(four)
    if max(li_sum) == one:
        print("The list with highest sum is : ", li_one)
        print("List one.")

    elif max(li_sum) == two:
        print("The list with highest sum is : ", li_two)
        print("List two.")

    elif max(li_sum) == three:
        print("The list with highest sum is : ", li_three)
        print("List three.")

    elif max(li_sum) == four:
        print("The list with highest sum is : ", li_four)
        print("List four.")

    x = input("Do you wish to retry? ").lower()
    if x == "yes":
        continue
    else:
        break


