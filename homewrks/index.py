
li_length = int(input("Maximum students in the cohort: "))
count = 0
li_cohort = []
print("Options: 1.Fill in cohort, 2.Add a new student, 3.Remove a student,"
      "4.List the students in the cohort, 5.Show number of students in  the cohort")
option = int(input("What option will you carry out? "))

if option == 1:
    count = 0
    while count < li_length:
       name = input("Enter the names of students:")
       li_cohort.append(name)
       count = count + 1

elif option == 2:
    new = input("Enter name of student: ")
    pos = int(input("At what position will you place the new student? "))
    if pos < li_cohort.len:
        li_cohort.insert(pos, new)
    else:
        print("That position is not in the cohort.")

elif option == 3:
    excluded = input("Name of student to be removed?")
    if excluded in li_cohort:
        li_cohort.remove(excluded)
    else:
        print("The name you entered is not in the Cohort.")

elif option == 4:
    print(li_cohort)

elif option == 5:
    print("Your cohort has ", + li_cohort)






