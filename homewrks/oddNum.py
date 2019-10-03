while True:
    number = input("Please enter a positive number: ")
    print("0")
    if number.isdigit():
        range(0, (int(number) + 1))
        for i in range(0, (int(number) + 1)):
            if i % 2 != 0:

                print(i)
    else:
        print("What you entered must not be a number or a negative number. Please be serious.")
