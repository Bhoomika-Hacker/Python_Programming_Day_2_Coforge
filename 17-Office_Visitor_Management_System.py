visitors = []

while True:
    print("\n==========================================")
    print("     Office Visitor Management System")
    print("==========================================")
    print("1. Add Visitor")
    print("2. View Visitors")
    print("3. Search Visitor")
    print("4. Update Visitor")
    print("5. Remove Visitor")
    print("6. Total Visitors")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Visitor Name: ")
        address = input("Enter Visitor Address: ")
        phone = input("Enter Visitor Phone No: ")
        email = input("Enter Visitor Email: ")
        city = input("Enter Visitor City: ")

        visitors.append(name)
        print("Visitor added successfully.")

    elif choice == "2":
        if len(visitors) == 0:
            print("No visitor records found.")
        else:
            print("\nToday's Visitors")
            for i in range(len(visitors)):
                print(i + 1, "-", visitors[i])

    elif choice == "3":
        search = input("Enter Visitor Name to Search: ")

        if search in visitors:
            print("Visitor Found.")
        else:
            print("Visitor Not Found.")

    elif choice == "4":
        if len(visitors) == 0:
            print("No visitor records found.")
        else:
            print("\nVisitor List")
            for i in range(len(visitors)):
                print(i + 1, "-", visitors[i])

            number = int(input("Enter Visitor Number: "))

            if number >= 1 and number <= len(visitors):
                new_name = input("Enter New Visitor Name: ")
                visitors[number - 1] = new_name
                print("Visitor details updated successfully.")
            else:
                print("Invalid Visitor Number.")

    elif choice == "5":
        if len(visitors) == 0:
            print("No visitor records found.")
        else:
            print("\nVisitor List")
            for i in range(len(visitors)):
                print(i + 1, "-", visitors[i])

            number = int(input("Enter Visitor Number: "))

            if number >= 1 and number <= len(visitors):
                visitors.pop(number - 1)
                print("Visitor removed successfully.")
            else:
                print("Invalid Visitor Number.")

    elif choice == "6":
        print("Total Visitors Today :", len(visitors))

    elif choice == "7":
        print("Thank you for using Office Visitor Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")