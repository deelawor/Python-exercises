#The highest common factor (H.C.F) of two numbers
# is the largest positive integer that perfectly
# divides the two given numbers


def computeHCF(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    #i is a number in the range 1 - smaller+1.
    #if there is an "i" within that range that gives
    # zero remainder with x and y i will be our hcf

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


while True:
    num1 = int(input("Enter a positive integer: "))
    num2 = int(input("Enter a positive integer: "))

    print("The H.C.F. of", num1, "and", num2, "is", computeHCF(num1, num2))

    x = input("Do you wish to retry? ").lower()
    if x == "yes":
        continue
    else:
        break

#https://www.programiz.com/python-programming/examples/hcf