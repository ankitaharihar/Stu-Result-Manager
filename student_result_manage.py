student = {}

while True:
    print("\n---- Student Management App ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        mark = int(input("Enter Marks: "))

        student[name] = mark

        print(f"{name} Successfully Added!")

    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, mark in student.items():
                print(name, ":", mark)

    elif choice == "3":
        name = input("Enter Student Name: ")

        if name in student:
            mark = student[name]

            if mark >= 40:
                print("Pass")
            else:
                print("Fail")

        else:
            print("Student not found!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input!")