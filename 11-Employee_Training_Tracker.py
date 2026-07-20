Employees = []

while True:
    print("\n----------------------------------------")
    print("Employee Training Tracker System")
    print("----------------------------------------")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")
    choice = input("Enter your choice (1-4):")
    if choice == '1':
        employee_name = input("Enter Employee Name: ")
        employee_id = input("Enter Employee ID: ")
        salary  = float(input("Enter Employee Salary:"))
        Designation = input("Enter Employee Designation: ")
        employee_skills = input("Enter Employee Skills (comma-separated): ").split(",")
        employee_skills = [skill.strip() for skill in employee_skills]
        employee = {
            "name": employee_name,
            "id": employee_id,
            "Salary": salary,
            "Designation": Designation,
            "skills": employee_skills
        }
        Employees.append(employee)
        print(f"Employee {employee_name} added successfully.")
    elif choice == '2':
        if len(Employees) == 0:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for emp in Employees:
                print(f"Name: {emp['name']}, ID: {emp['id']}, Skills: {', '.join(emp['skills'])}")
    elif choice == '3':
        search_id = input("Enter Employee ID to search: ")
        found = False
        for emp in Employees:
            if emp['id'] == search_id:
                print(f"Employee Found: Name: {emp['name']}, ID: {emp['id']}, Skills: {', '.join(emp['skills'])}")
                found = True
                break
        if not found:
            print("Employee not found.")
    elif choice == '4':
        print("Exiting Employee Training Tracker System.")
        break
    else:
        print("Invalid choice. Please try again.")