#The least common multiple (L.C.M.) of two numbers
# is the smallest positive integer
# that is perfectly divisible by the two given numbers.


def computeLCM(x, y):

    if x > y :
        largest = x
    else:
       largest = y

     #incrementing largest until
     #largest gives no remainder
     #by neither x or y.

    while True:
        if((largest % x == 0) and (largest % y == 0)):
            lcm = largest
            break
        largest += 1
    return lcm


while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("The L.C.M. of", num1,"and", num2,"is", computeLCM(num1, num2))

    x = input("Do you wish to retry? ").lower()
    if x == "yes":
        continue
    else:
        break

#https://www.programiz.com/python-programming/examples/lcm

