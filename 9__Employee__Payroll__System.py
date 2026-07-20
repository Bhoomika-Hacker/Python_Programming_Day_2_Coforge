employees = []

def enter_employee_details():
    employee = {}

    while True:
        employee["id"] = input("Enter Employee ID: ")
        if employee["id"] != "":
            break
        print("Employee ID cannot be empty")

    while True:
        employee["name"] = input("Enter Employee Name: ")
        if employee["name"] != "":
            break
        print("Employee Name cannot be empty")

    while True:
        employee["basic"] = float(input("Enter Basic Salary: "))
        if employee["basic"] > 0:
            break
        print("Basic Salary must be greater than zero")

    while True:
        employee["overtime"] = float(input("Enter Number of Overtime Hours: "))
        if employee["overtime"] >= 0:
            break
        print("Overtime hours cannot be negative")

    while True:
        employee["leave"] = int(input("Enter Number of Leave Days: "))
        if employee["leave"] >= 0:
            break
        print("Leave days cannot be negative")

    employees.append(employee)

    print("\nEmployee Details Entered Successfully")


def calculate_monthly_payroll():
    if len(employees) == 0:
        print("\nPlease enter employee details first")
        return

    for employee in employees:
        employee["hra"] = employee["basic"] * 0.20
        employee["da"] = employee["basic"] * 0.10
        employee["overtime_payment"] = employee["overtime"] * 500

        employee["gross_salary"] = (
            employee["basic"] +
            employee["hra"] +
            employee["da"] +
            employee["overtime_payment"]
        )

        employee["pf"] = employee["basic"] * 0.12
        employee["professional_tax"] = 500
        employee["leave_deduction"] = employee["leave"] * 100

        employee["total_deduction"] = (
            employee["pf"] +
            employee["professional_tax"] +
            employee["leave_deduction"]
        )

        employee["net_salary"] = (
            employee["gross_salary"] -
            employee["total_deduction"]
        )

    print("\nMonthly Payroll Calculated Successfully")


def display_salary_slip():
    if len(employees) == 0:
        print("\nPlease enter employee details first")
        return

    if "net_salary" not in employees[0]:
        print("\nPayroll cannot be displayed before calculation")
        return

    for employee in employees:
        print("\n----------------------------------------")
        print("          EMPLOYEE SALARY SLIP")
        print("----------------------------------------")
        print(f"Employee ID       : {employee['id']}")
        print(f"Employee Name     : {employee['name']}")
        print(f"Basic Salary      : ₹{employee['basic']:,.2f}")
        print(f"HRA               : ₹{employee['hra']:,.2f}")
        print(f"DA                : ₹{employee['da']:,.2f}")
        print(f"Overtime Payment  : ₹{employee['overtime_payment']:,.2f}")
        print(f"Gross Salary      : ₹{employee['gross_salary']:,.2f}")
        print(f"PF Deduction      : ₹{employee['pf']:,.2f}")
        print(f"Professional Tax  : ₹{employee['professional_tax']:,.2f}")
        print(f"Leave Deduction   : ₹{employee['leave_deduction']:,.2f}")
        print(f"Total Deduction   : ₹{employee['total_deduction']:,.2f}")
        print(f"Net Salary        : ₹{employee['net_salary']:,.2f}")
        print("----------------------------------------")


def calculate_annual_net_salary():
    if len(employees) == 0:
        print("\nPlease enter employee details first")
        return

    if "net_salary" not in employees[0]:
        print("\nPlease calculate monthly payroll first")
        return

    for employee in employees:
        annual_salary = employee["net_salary"] * 12

        print("\nEmployee Name:", employee["name"])
        print(f"Annual Net Salary : ₹{annual_salary:,.2f}")


while True:

    print("\nMenu Operations")
    print("1. Enter Employee Details")
    print("2. Calculate Monthly Payroll")
    print("3. Display Salary Slip")
    print("4. Calculate Annual Net Salary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enter_employee_details()

    elif choice == 2:
        calculate_monthly_payroll()

    elif choice == 3:
        display_salary_slip()

    elif choice == 4:
        calculate_annual_net_salary()

    elif choice == 5:
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice")