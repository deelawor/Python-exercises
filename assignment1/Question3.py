while True:
    reverseNum = []
    num = []
    i=0
    number = input("Enter a number: ")
    for n in number:
        reverseNum.append(n)
        num.append(n)

    lD = reverseNum[-1]

    fD = reverseNum[0]#lD-last digit, fD-first digit

    reverseNum.remove(lD)
    reverseNum.remove(fD)

    a = reverseNum.append(fD)
    b = reverseNum.insert(0, lD)

    if num == reverseNum:
        print("True")

    else:
        print("Not True")

    x = input("Do you wish to input another number? ").lower()
    if x == "yes":
        continue
    else:
        break



