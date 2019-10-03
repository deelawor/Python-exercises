while True:

    lower = 0
    upper = 0
    digit = 0
    specialChar = 0
    sen = input("Enter a sentence: ")

    for x in sen:
        if x.islower() == True:
            lower = lower + 1

        elif x.isupper() == True:
            upper = upper + 1

        elif x.isdigit() == True:
            digit = digit + 1

        elif x.isalnum() != True:
            specialChar = specialChar + 1

    print("Number of lower case alphabet: ", lower)
    print("Number of upper case alphabet: ", upper)
    print("Number of digits: ", digit)
    print("Number of special Characters: ", specialChar, ". Spaces count as special character in this program.")
    x = input("Do you wish to retry? ").lower()
    if x == "yes":
        continue
    else:
        break
