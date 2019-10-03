while True:
    alphabet = input("Please enter an alphabet: ")

    if alphabet.isalpha():
        a = alphabet.upper()
        if a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
            print("The character " + alphabet + " is a vowel.")
            print("Press \"#\" if you want to exit program.")
        else:
            print("The character " + alphabet + " is a consonant.")
            print("Press \"#\" if you want to exit program.")
    else:
        print("What you entered is not an alphabet. Retry")

        if a == "#":
            break
