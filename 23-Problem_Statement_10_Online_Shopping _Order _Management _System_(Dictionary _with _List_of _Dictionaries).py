customers = [
    {
        "CustomerId": 101,
        "CustomerName": "Rahul Sharma",
        "City": "Noida",
        "Orders": [
            {
                "ProductId": 1,
                "ProductName": "Laptop",
                "Quantity": 1,
                "Price": 65000
            },
            {
                "ProductId": 2,
                "ProductName": "Mouse",
                "Quantity": 2,
                "Price": 800
            }
        ]
    },
    {
        "CustomerId": 102,
        "CustomerName": "Priya Singh",
        "City": "Delhi",
        "Orders": [
            {
                "ProductId": 3,
                "ProductName": "Keyboard",
                "Quantity": 1,
                "Price": 2500
            }
        ]
    }
]

while True:
    print("\n" + "=" * 60)
    print("        ONLINE SHOPPING ORDER MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Add New Customer")
    print("2. Add Product Order")
    print("3. View All Customers and Their Orders")
    print("4. Search Customer")
    print("5. Update Product Quantity")
    print("6. Remove a Product")
    print("7. Calculate Total Order Value")
    print("8. Display Customer with Maximum Order Value")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cid = int(input("Enter Customer ID: "))
        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                found = True
                break

        if found:
            print("Customer ID already exists.")
        else:
            name = input("Enter Customer Name: ")
            city = input("Enter City: ")

            customer = {
                "CustomerId": cid,
                "CustomerName": name,
                "City": city,
                "Orders": []
            }

            customers.append(customer)
            print("Customer added successfully.")

    elif choice == 2:
        cid = int(input("Enter Customer ID: "))
        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                found = True

                pid = int(input("Enter Product ID: "))
                pname = input("Enter Product Name: ")
                qty = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))

                product = {
                    "ProductId": pid,
                    "ProductName": pname,
                    "Quantity": qty,
                    "Price": price
                }

                customer["Orders"].append(product)
                print("Product order added successfully.")
                break

        if not found:
            print("Customer not found.")

    elif choice == 3:
        if len(customers) == 0:
            print("No customers available.")
        else:
            for customer in customers:
                print("\nCustomer ID :", customer["CustomerId"])
                print("Customer Name :", customer["CustomerName"])
                print("City :", customer["City"])
                print("\nOrders")

                if len(customer["Orders"]) == 0:
                    print("No Orders")
                else:
                    for product in customer["Orders"]:
                        print("Product ID :", product["ProductId"])
                        print("Product Name :", product["ProductName"])
                        print("Quantity :", product["Quantity"])
                        print("Price :", product["Price"])
                        print()

                print("-" * 40)

    elif choice == 4:
        cid = int(input("Enter Customer ID: "))
        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                found = True
                print("\nCustomer ID :", customer["CustomerId"])
                print("Customer Name :", customer["CustomerName"])
                print("City :", customer["City"])
                print("\nOrders")

                if len(customer["Orders"]) == 0:
                    print("No Orders")
                else:
                    for product in customer["Orders"]:
                        print("Product ID :", product["ProductId"])
                        print("Product Name :", product["ProductName"])
                        print("Quantity :", product["Quantity"])
                        print("Price :", product["Price"])
                        print()
                break

        if not found:
            print("Customer not found.")

    elif choice == 5:
        cid = int(input("Enter Customer ID: "))
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter New Quantity: "))

        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                for product in customer["Orders"]:
                    if product["ProductId"] == pid:
                        product["Quantity"] = qty
                        print("Quantity updated successfully.")
                        found = True
                        break
                break

        if not found:
            print("Customer or Product not found.")

    elif choice == 6:
        cid = int(input("Enter Customer ID: "))
        pid = int(input("Enter Product ID: "))

        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                for product in customer["Orders"]:
                    if product["ProductId"] == pid:
                        customer["Orders"].remove(product)
                        print("Product removed successfully.")
                        found = True
                        break
                break

        if not found:
            print("Customer or Product not found.")

    elif choice == 7:
        cid = int(input("Enter Customer ID: "))
        found = False

        for customer in customers:
            if customer["CustomerId"] == cid:
                found = True
                total = 0

                print("\nOrder Details")

                for product in customer["Orders"]:
                    amount = product["Quantity"] * product["Price"]
                    total += amount
                    print(product["ProductName"], ":", amount)

                print("-" * 25)
                print("Total Bill :", total)
                break

        if not found:
            print("Customer not found.")

    elif choice == 8:
        if len(customers) == 0:
            print("No customers available.")
        else:
            max_customer = None
            max_total = 0

            for customer in customers:
                total = 0

                for product in customer["Orders"]:
                    total += product["Quantity"] * product["Price"]

                if total > max_total:
                    max_total = total
                    max_customer = customer

            if max_customer:
                print("\nCustomer Name :", max_customer["CustomerName"])
                print("Total Amount :", max_total)

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")