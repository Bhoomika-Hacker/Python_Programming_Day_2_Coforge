universities = [
    {
        "University": ("MRIIRS", 1),
        "Students": [
            ("Bhoomika", 24, "CSE", 101)
        ]
    },
    {
        "University": ("MRU", 2),
        "Students": [
            ("Rahul", 22, "IT", 201)
        ]
    }
]

while True:

    print("\n--------------------------------------")
    print("     University Management System")
    print("--------------------------------------")
    print("1. Add University")
    print("2. View All University")
    print("3. Add Student to University")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        university_name = input("Enter University Name: ")
        university_id = int(input("Enter University ID: "))

        duplicate = False

        for university in universities:

            if university["University"][1] == university_id:
                print("University ID is already assigned to", university["University"][0])
                duplicate = True
                break

            if university["University"][0].lower() == university_name.lower():
                print("This university already exists.")
                duplicate = True
                break

        if not duplicate:

            universities.append({
                "University": (university_name, university_id),
                "Students": []
            })

            print("University added successfully.")

    elif choice == "2":

        for university in universities:

            print("\n======================================")
            print("University Name :", university["University"][0])
            print("University ID   :", university["University"][1])
            print("======================================")

            if len(university["Students"]) == 0:
                print("No Students Available.")

            else:

                for student in university["Students"]:

                    print("Name       :", student[0])
                    print("Age        :", student[1])
                    print("Branch     :", student[2])
                    print("Student ID :", student[3])
                    print("--------------------------------")

    elif choice == "3":

        print("\nAvailable Universities")

        for university in universities:
            print(university["University"][1], "-", university["University"][0])

        university_id = int(input("\nEnter University ID: "))

        found = False

        for university in universities:

            if university["University"][1] == university_id:

                found = True

                print("Selected University:", university["University"][0])

                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                branch = input("Enter Branch: ")
                student_id = int(input("Enter Student ID: "))

                duplicate = False

                for uni in universities:

                    for student in uni["Students"]:

                        if student[3] == student_id:

                            print("Student ID is already assigned to", student[0])
                            duplicate = True
                            break

                    if duplicate:
                        break

                if not duplicate:

                    university["Students"].append(
                        (name, age, branch, student_id)
                    )

                    print("Student added successfully to", university["University"][0])

                break

        if not found:
            print("University ID not found.")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice.")