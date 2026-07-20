print("=" * 50)
print("EMPLOYEE ID PROCESSING SYSTEM")
print("=" * 50)

# Employee ID Processing System

n = int(input("Enter the number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    Employee_Name = input("Enter Employee Name: ")
    Employee_ID = int(input("Enter Employee ID: "))

    # Stop processing if Employee ID is 37
    if Employee_ID == 37:
        print("Critical termination encountered at Employee ID:", Employee_ID)
        break

    # Skip Employee IDs divisible by 5
    if Employee_ID % 5 == 0:
        print("Employee ID", Employee_ID, "is divisible by 5.")
        print("Maintenance record. Processing skipped.")
        continue

    # Print only Employee IDs greater than 20
    if Employee_ID > 20:
        print("\nEmployee Details")
        print("Employee Name :", Employee_Name)
        print("Employee ID   :", Employee_ID)
    else:
        print("Employee ID is 20 or below. Not processed.")