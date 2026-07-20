# ==========================================
# CONTINUE STATEMENT PROGRAMS (11 - 20)
# ==========================================

# 11. Skip Inactive Employees
print("11. Skip Inactive Employees")
employees = [
    ("Amit", "Active"),
    ("Riya", "Inactive"),
    ("Karan", "Active"),
    ("Neha", "Inactive"),
    ("Rahul", "Active")
]

for name, status in employees:
    if status == "Inactive":
        continue
    print(name, "-", status)

print()


# 12. Ignore Weekend Sales Data
print("12. Ignore Weekend Sales Data")
sales = {
    "Monday": 5000,
    "Tuesday": 6000,
    "Wednesday": 5500,
    "Thursday": 7000,
    "Friday": 6500,
    "Saturday": 8000,
    "Sunday": 7500
}

total_sales = 0

for day in sales:
    if day == "Saturday" or day == "Sunday":
        continue
    total_sales += sales[day]

print("Working Day Sales =", total_sales)

print()


# 13. Skip Invalid Email Addresses
print("13. Skip Invalid Email Addresses")
emails = [
    "abc@gmail.com",
    "hello123",
    "user@yahoo.com",
    "testmail",
    "admin@company.com"
]

for email in emails:
    if "@" not in email:
        continue
    print("Mail sent to:", email)

print()


# 14. Ignore Null Sensor Readings
print("14. Ignore Null Sensor Readings")
temperatures = [30, 32, None, 28, None, 35, 31]

for temp in temperatures:
    if temp is None:
        continue
    print("Temperature:", temp)

print()


# 15. Skip Failed Student Submissions
print("15. Skip Failed Student Submissions")
submissions = {
    "Amit": True,
    "Riya": False,
    "Karan": True,
    "Neha": False,
    "Rahul": True
}

for student in submissions:
    if submissions[student] == False:
        continue
    print("Evaluating:", student)

print()


# 16. Filter Out Negative Values
print("16. Filter Out Negative Values")
numbers = [15, -5, 20, 35, -10, 25, 40]

total = 0
count = 0

for num in numbers:
    if num < 0:
        continue
    total += num
    count += 1

average = total / count

print("Average =", average)

print()


# 17. Leave Processing for Eligible Employees
print("17. Leave Processing for Eligible Employees")
employees = [
    ("Amit", "Permanent"),
    ("Riya", "Contract"),
    ("Karan", "Permanent"),
    ("Neha", "Contract"),
    ("Rahul", "Permanent")
]

for name, emp_type in employees:
    if emp_type == "Contract":
        continue
    print("Leave processed for:", name)

print()


# 18. Skip Duplicate User IDs
print("18. Skip Duplicate User IDs")
user_ids = [101, 102, 103, 101, 104, 105, 102, 106]

processed = []

for uid in user_ids:
    if uid in processed:
        continue
    processed.append(uid)
    print("Migrated User ID:", uid)

print()


# 19. Ignore Comment Lines in File
print("19. Ignore Comment Lines in File")
lines = [
    "# Configuration File",
    "host=localhost",
    "# Database Settings",
    "port=3306",
    "username=root",
    "# End"
]

for line in lines:
    if line.startswith("#"):
        continue
    print("Processing:", line)

print()


# 20. Skip Low Priority Tickets
print("20. Skip Low Priority Tickets")
tickets = [
    ("T101", "High"),
    ("T102", "Low"),
    ("T103", "Medium"),
    ("T104", "Low"),
    ("T105", "High")
]

for ticket, priority in tickets:
    if priority == "Low":
        continue
    print(ticket, "-", priority)

print("\nAll programs executed successfully.")