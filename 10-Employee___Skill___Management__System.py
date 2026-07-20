Employee_skills = ["Python", "Java", "C++", "SQL", "HTML", "CSS", "JavaScript"]

while True:
    print("\n----------------------------------------")
    print("Employee Skill Management System")
    print("----------------------------------------")
    print("1. Display Skill")
    print("2. Add Skill")
    print("3. Insert Skill")
    print("4. Update Skill")
    print("5. Remove Skill")
    print("6. Search Skill")
    print("7. Count Skills")
    print("8. Sort Skill")
    print("9. Reverse Skill")
    print("10. Copy Skill")
    print("11. Clear Skill")
    print("12. Display Skills By enumerate")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")

    if choice == '1':
        if len(Employee_skills) == 0:
            print("No Skills available.")
        else:
            print("\nEmployee Skills:")
            count = 1 
            for skill in Employee_skills:
                print(f"{count}. {skill}")
                count = count + 1

    elif choice == '2':
        skill = input("Enter the skill to add: ")
        if skill not in Employee_skills:
            Employee_skills.append(skill)
            print(f"{skill} has been added.")
        else:
            print(f"{skill} already exists.")

    elif choice == '3':
        skill = input("Enter the skill to insert: ")
        position = int(input("Enter position number: "))

        Employee_skills.insert(position, skill)
        print(f"{skill} inserted successfully.")

    elif choice == '4':
        update_skill = input("Enter skill to update: ")

        if update_skill in Employee_skills:
            updated_skill = input("Enter new skill name: ")
            index = Employee_skills.index(update_skill)
            Employee_skills[index] = updated_skill
            print("Skill updated successfully.")
        else:
            print("Skill not found.")
    elif choice == '5':
        delete_skill = input("Enter skill to delete: ")

        if delete_skill in Employee_skills:
            Employee_skills.remove(delete_skill)
            print("Skill deleted successfully.")
        else:
            print("Skill not found.")
    elif choice == '6':
        search_skill = input("Enter skill to search: ")

        if search_skill in Employee_skills:
            print(f"{search_skill} is present in the list.")
        else:
            print(f"{search_skill} is not found in the list.")
    elif choice == '7':
        print(f"Total number of skills: {len(Employee_skills)}")
    elif choice == '8':
        Employee_skills.sort()
        print("Skills sorted successfully.")
    elif choice == '9':
        Employee_skills.reverse()
        print("Skills reversed successfully.")
    elif choice == '10':
        copied_skills = Employee_skills.copy()
        print("Skills copied successfully.")
        print("Copied Skills:", copied_skills)
    elif choice == '11':
        Employee_skills.clear()
        print("All skills cleared successfully.")
    elif choice == '12':
        print("Skills displayed with enumeration:")
        for i, skill in enumerate(Employee_skills, start=1):
            print(f"{i}. {skill}")
    elif choice == '13':
        print("Exiting the Employee Skill Management System.")
        break
    else:
        print("Invalid choice. Please enter between 1-12.")