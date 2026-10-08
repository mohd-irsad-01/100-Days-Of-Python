students = []
while True:
    print("\n==== STUDENT MANAGEMENT SYSTEM ====")
    print("1. Add Student")
    print("2. Didplay Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    #Add Student
    if choice == 1:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("\nStudent added successfully!")

    # Display Students
    elif choice == 2:
        if len(students) == 0:
            print("\nNo students found.")
        else:
            print("\n==== STUDENT DETAILS ====")
            for student in students:
                print("\nName   :", student["name"])
                print("\nage   :", student["age"])
                print("\ncourse   :", student["course"])

    # Search Student
    elif choice == 3:
        name = input("Enter student name: ")
        found = False
        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent found!")
                print("Name   :", student["name"])
                print("Age   :", student["age"])
                print("Course   :", student["course"])

                found = True
                break

            if found == False:
                print("\nStudent not found")

    # Delete Student
    elif choice == 4:
        name = input("Enter student name: ")
        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("\nStudent deleted successfully!")
                break
            else:
                print("\nStudent not found.")

    # Exit
    elif choice == 5:
        print("\nThank you for using Student Management System!")
        break

    # Invalid Choice
    else:
        print("\nInvalid choice! Please try again.")
