employees = [
    (101, "Rahul", "AI", ["Chatbot", "Resume Analyzer"]),
    (102, "Priya", "Cloud", ["Azure Migration"]),
    (103, "Amit", "Python", ["Payroll System", "Inventory", "Billing"])
]

while True:
    print("\n" + "=" * 60)
    print("        Employee Project Management System")
    print("=" * 60)
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Assign a New Project")
    print("4. Remove a Project")
    print("5. Search Employee")
    print("6. Display Employees Working on Multiple Projects")
    print("7. Display Department-wise Employee Count")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))

        found = False
        for emp in employees:
            if emp[0] == emp_id:
                print("Employee ID already exists.")
                found = True
                break

        if not found:
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            n = int(input("Enter Number of Projects: "))
            project_list = []

            for i in range(n):
                project = input(f"Enter Project {i + 1}: ")
                project_list.append(project)

            employees.append((emp_id, name, department, project_list))
            print("Employee added successfully.")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print()
            for emp in employees:
                print("Employee ID :", emp[0])
                print("Name        :", emp[1])
                print("Department  :", emp[2])
                if len(emp[3]) > 0:
                    print("Projects    :", ", ".join(emp[3]))
                else:
                    print("Projects    : None")
                print("-" * 45)

    elif choice == "3":
        emp_id = int(input("Enter Employee ID: "))
        found = False

        for emp in employees:
            if emp[0] == emp_id:
                project = input("Enter New Project Name: ")
                if project in emp[3]:
                    print("Project already assigned.")
                else:
                    emp[3].append(project)
                    print("Project assigned successfully.")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        emp_id = int(input("Enter Employee ID: "))
        found = False

        for emp in employees:
            if emp[0] == emp_id:
                project = input("Enter Project Name to Remove: ")

                if project in emp[3]:
                    emp[3].remove(project)
                    print("Project removed successfully.")
                else:
                    print("Project not found.")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "5":
        emp_id = int(input("Enter Employee ID: "))
        found = False

        for emp in employees:
            if emp[0] == emp_id:
                print("\nEmployee Found")
                print("Employee ID :", emp[0])
                print("Name        :", emp[1])
                print("Department  :", emp[2])
                if len(emp[3]) > 0:
                    print("Projects    :", ", ".join(emp[3]))
                else:
                    print("Projects    : None")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "6":
        found = False
        print("\nEmployees Working on Multiple Projects\n")

        for emp in employees:
            if len(emp[3]) > 2:
                print(emp[1])
                print("Projects :", len(emp[3]))
                print("-" * 30)
                found = True

        if not found:
            print("No employee is working on more than two projects.")

    elif choice == "7":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            departments = []

            for emp in employees:
                if emp[2] not in departments:
                    departments.append(emp[2])

            print()

            for dept in departments:
                count = 0
                for emp in employees:
                    if emp[2] == dept:
                        count += 1
                print(f"{dept:<10}: {count}")

    elif choice == "8":
        print("Thank You")
        break

    else:
        print("Invalid choice.")