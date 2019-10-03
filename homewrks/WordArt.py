for row in range(5):
    for col in range(4):
        if ((col == 0 or col == 3) and row != 0) or ((row == 0 or row == 2) and (col > 0 or col < 3)):
            print("*", end="")
        else:
            print(end=" ")
    print()

print()

for row in range(5):
    for col in range(4):
        if ((col== 0 or col == 3) and row != 4) or (row == 4 and ( col > 0 or col < 3)):
            print("*", end="")
        else:
            print(end=" ")
    print()

print()

for row in range(5):
    for col in range(5):
        if  :
            print("*", end="")
        else:
            print(end=" ")
    print()


