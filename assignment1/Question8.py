print("Rock, Paper, Scissors Game: ")
while True:
    print("Player One")
    x = input("Enter your play: ").lower()

    print("Player Two")
    y = input("Enter your play: ").lower()

    if x == y:
        print("Draw.")
    elif x == "rock" and y == "paper":
        print("Congratulations, Player Two wins!")
    elif x == "rock" and y == "scissors":
        print("Congratulations, Player One wins!")
    elif x == "paper" and y == "rock":
        print("Congratulations, Player One wins!")
    elif x == "paper" and y == "scissors":
        print("Congratulations, Player Two wins!")
    elif x == "scissors" and y == "paper":
        print("Congratulations, Player One wins!")
    elif x == "scissors" and y == "rock":
        print("Congratulations, Player Two wins!")

    ans = input("Do you want to play again? ").lower()
    if ans == "yes":
        continue
    else:
        print("Thanks for playing!")
        break

