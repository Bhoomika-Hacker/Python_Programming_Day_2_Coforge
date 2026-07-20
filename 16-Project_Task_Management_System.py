tasks = []

while True:

    print("\n==============================================")
    print("       Project Task Management System")
    print("==============================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Count Tasks")
    print("7. Exit")
    print("==============================================")

    choice = input("Enter your choice: ")

    # Operation 1 - Add Task
    if choice == "1":

        task_name = input("Enter Task Name: ")

        tasks.append(task_name)

        print("\nTask added successfully.")


    # Operation 2 - View Tasks
    elif choice == "2":

        print("\nProject Tasks")

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            for i in range(len(tasks)):

                print(i + 1, "-", tasks[i])


    # Operation 3 - Search Task
    elif choice == "3":

        search_task = input("Enter Task Name to Search: ")

        found = False

        for task in tasks:

            if task.lower() == search_task.lower():

                found = True
                break

        if found:

            print("Task Found.")

        else:

            print("Task Not Found.")


    # Operation 4 - Update Task
    elif choice == "4":

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            print("\nProject Tasks")

            for i in range(len(tasks)):

                print(i + 1, "-", tasks[i])


            task_number = int(input("\nEnter Task Number to Update: "))


            if task_number > 0 and task_number <= len(tasks):

                new_task = input("Enter New Task: ")

                tasks[task_number - 1] = new_task

                print("\nTask updated successfully.")

            else:

                print("Invalid Task Number.")



    # Operation 5 - Delete Task
    elif choice == "5":

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            print("\nProject Tasks")

            for i in range(len(tasks)):

                print(i + 1, "-", tasks[i])


            task_number = int(input("\nEnter Task Number to Delete: "))


            if task_number > 0 and task_number <= len(tasks):

                tasks.pop(task_number - 1)

                print("\nTask deleted successfully.")

            else:

                print("Invalid Task Number.")



    # Operation 6 - Count Tasks
    elif choice == "6":

        print("\nTotal Project Tasks :", len(tasks))



    # Operation 7 - Exit
    elif choice == "7":

        print("\nThank you for using Project Task Management System.")

        break


    else:

        print("Invalid Choice. Please select between 1-7.")