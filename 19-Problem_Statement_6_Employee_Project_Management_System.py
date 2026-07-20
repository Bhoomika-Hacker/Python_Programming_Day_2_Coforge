employee = (
    101,
    "Gaurav Joshi",
    "AI Developer",
    ["Payroll System", "HR Portal"]
)

while True:
    print("\n" + "=" * 55)
    print("        Employee Project Management System")
    print("=" * 55)
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove a Project")
    print("4. Search a Project")
    print("5. Display Total Number of Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEmployee ID      :", employee[0])
        print("Employee Name    :", employee[1])
        print("Department       :", employee[2])
        print("Assigned Projects:")
        if len(employee[3]) == 0:
            print("No Projects Assigned.")
        else:
            for project in employee[3]:
                print(project)

    elif choice == 2:
        project = input("Enter Project Name: ")
        employee[3].append(project)
        print("Project added successfully.")

    elif choice == 3:
        project = input("Enter Project Name: ")
        if project in employee[3]:
            employee[3].remove(project)
            print("Project removed successfully.")
        else:
            print("Project not found.")

    elif choice == 4:
        project = input("Enter Project Name: ")
        if project in employee[3]:
            print("Project Assigned.")
        else:
            print("Project Not Assigned.")

    elif choice == 5:
        print("Total Projects :", len(employee[3]))

    elif choice == 6:
        print("\nProjects in Alphabetical Order:")
        for project in sorted(employee[3]):
            print(project)

    elif choice == 7:
        print("Exiting Employee Project Management System...")
        break

    else:
        print("Invalid Choice! Please try again.")