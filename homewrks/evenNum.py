while True:
    number = input("Please enter a positive number: ")
    if number.isdigit():

        range(0, (int(number) + 1))
        for i in range(0, (int(number) + 1)):
            if i % 2 == 0:
                print(i)
    else:
        print("What you entered must not be a number or number is negative. Please be serious.")
