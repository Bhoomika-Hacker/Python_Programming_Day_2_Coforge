astronauts = [
    (201, "Neil", "NASA", ["Artemis I", "Lunar Research"]),
    (202, "Rakesh", "ISRO", ["Gaganyaan", "Orbital Training"]),
    (203, "Emma", "ESA", ["Mars Explorer", "Moon Base", "Deep Space Research"])
]

while True:
    print("\n" + "=" * 60)
    print("          ASTRONAUT MISSION MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Register New Astronaut")
    print("2. View All Astronauts")
    print("3. Assign New Mission")
    print("4. Complete (Remove) Mission")
    print("5. Search Astronaut")
    print("6. Display Experienced Astronauts")
    print("7. Display Space Agency-wise Astronaut Count")
    print("8. Exit")
    print("=" * 60)

    choice = input("Enter your choice: ")

    if choice == "1":
        astronaut_id = int(input("Enter Astronaut ID: "))

        found = False
        for astronaut in astronauts:
            if astronaut[0] == astronaut_id:
                found = True
                break

        if found:
            print("Astronaut ID already exists.")
        else:
            name = input("Enter Astronaut Name: ")
            agency = input("Enter Space Agency: ")
            n = int(input("Enter Number of Missions: "))
            missions = []

            for i in range(n):
                missions.append(input(f"Enter Mission {i + 1}: "))

            astronauts.append((astronaut_id, name, agency, missions))
            print("Astronaut registered successfully.")

    elif choice == "2":
        if len(astronauts) == 0:
            print("No astronauts available.")
        else:
            print()
            for astronaut in astronauts:
                print("-" * 45)
                print("Astronaut ID :", astronaut[0])
                print("Name         :", astronaut[1])
                print("Agency       :", astronaut[2])
                print("Missions     :", ", ".join(astronaut[3]))
            print("-" * 45)

    elif choice == "3":
        astronaut_id = int(input("Enter Astronaut ID: "))
        found = False

        for astronaut in astronauts:
            if astronaut[0] == astronaut_id:
                mission = input("Enter New Mission Name: ")
                astronaut[3].append(mission)
                print("Mission assigned successfully.")
                found = True
                break

        if not found:
            print("Astronaut not found.")

    elif choice == "4":
        astronaut_id = int(input("Enter Astronaut ID: "))
        found = False

        for astronaut in astronauts:
            if astronaut[0] == astronaut_id:
                found = True
                mission = input("Enter Mission Name to Remove: ")

                if mission in astronaut[3]:
                    astronaut[3].remove(mission)
                    print("Mission removed successfully.")
                else:
                    print("Mission not found.")
                break

        if not found:
            print("Astronaut not found.")

    elif choice == "5":
        astronaut_id = int(input("Enter Astronaut ID: "))
        found = False

        for astronaut in astronauts:
            if astronaut[0] == astronaut_id:
                print("-" * 45)
                print("Astronaut ID :", astronaut[0])
                print("Name         :", astronaut[1])
                print("Agency       :", astronaut[2])
                print("Missions     :", ", ".join(astronaut[3]))
                print("-" * 45)
                found = True
                break

        if not found:
            print("Astronaut not found.")

    elif choice == "6":
        found = False
        print()

        for astronaut in astronauts:
            if len(astronaut[3]) >= 3:
                print("-" * 35)
                print("Name           :", astronaut[1])
                print("Agency         :", astronaut[2])
                print("Total Missions :", len(astronaut[3]))
                found = True

        if not found:
            print("No experienced astronauts found.")

    elif choice == "7":
        agencies = []
        counts = []

        for astronaut in astronauts:
            if astronaut[2] in agencies:
                index = agencies.index(astronaut[2])
                counts[index] += 1
            else:
                agencies.append(astronaut[2])
                counts.append(1)

        print()
        for i in range(len(agencies)):
            print(f"{agencies[i]} : {counts[i]}")

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid choice.")