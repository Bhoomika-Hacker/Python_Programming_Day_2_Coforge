universities = [
    {
        "University": "MRIIRS",
        "University_ID": 1,
        "Students": [
            {
                "Name": "Bhoomika",
                "Age": 24,
                "Branch": "CSE",
                "Student_ID": 101
            }
        ]
    },
    {
        "University": "MRU",
        "University_ID": 2,
        "Students": [
            {
                "Name": "Rahul",
                "Age": 22,
                "Branch": "IT",
                "Student_ID": 201
            }
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

            if university.get("University_ID") == university_id:
                print("University ID is already assigned to", university.get("University"))
                duplicate = True
                break

            if university.get("University").lower() == university_name.lower():
                print("This university already exists.")
                duplicate = True
                break

        if not duplicate:

            universities.append({
                "University": university_name,
                "University_ID": university_id,
                "Students": []
            })

            print("University added successfully.")

    elif choice == "2":

        for university in universities:

            print("\n======================================")

            for key, value in university.items():

                if key != "Students":
                    print(key, ":", value)

            print("======================================")

            if len(university.get("Students")) == 0:
                print("No Students Available.")

            else:

                for student in university.get("Students"):

                    for key, value in student.items():
                        print(key, ":", value)

                    print("--------------------------------")

    elif choice == "3":

        print("\nAvailable Universities")

        for university in universities:
            print(university.get("University_ID"), "-", university.get("University"))

        university_id = int(input("\nEnter University ID: "))

        for university in universities:

            if university.get("University_ID") == university_id:

                print("Selected University:", university.get("University"))

                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                branch = input("Enter Branch: ")
                student_id = int(input("Enter Student ID: "))

                duplicate = False

                for uni in universities:

                    for student in uni.get("Students"):

                        if student.get("Student_ID") == student_id:
                            print("Student ID is already assigned to", student.get("Name"))
                            duplicate = True
                            break

                    if duplicate:
                        break

                if not duplicate:

                    university.get("Students").append({
                        "Name": name,
                        "Age": age,
                        "Branch": branch,
                        "Student_ID": student_id
                    })

                    print("Student added successfully to", university.get("University"))

                break

        else:
            print("University ID not found.")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice.")