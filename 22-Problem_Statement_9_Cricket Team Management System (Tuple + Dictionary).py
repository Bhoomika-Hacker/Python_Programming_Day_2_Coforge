players = [
    (
        101,
        "Virat Kohli",
        "India",
        {
            "Matches": 295,
            "Runs": 14181,
            "Centuries": 51,
            "HalfCenturies": 74
        }
    ),
    (
        102,
        "Joe Root",
        "England",
        {
            "Matches": 180,
            "Runs": 13500,
            "Centuries": 36,
            "HalfCenturies": 62
        }
    ),
    (
        103,
        "Steve Smith",
        "Australia",
        {
            "Matches": 170,
            "Runs": 11250,
            "Centuries": 34,
            "HalfCenturies": 45
        }
    )
]

while True:
    print("\n" + "=" * 60)
    print("           CRICKET TEAM MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Register New Player")
    print("2. View All Players")
    print("3. Update Player Statistics")
    print("4. Search Player")
    print("5. Display Highest Run Scorer")
    print("6. Display Players with More Than 10 Centuries")
    print("7. Team-wise Player Count")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        player_id = int(input("Enter Player ID: "))

        found = False
        for player in players:
            if player[0] == player_id:
                print("Player ID already exists.")
                found = True
                break

        if not found:
            name = input("Enter Player Name: ")
            team = input("Enter Team Name: ")
            matches = int(input("Enter Matches Played: "))
            runs = int(input("Enter Total Runs: "))
            centuries = int(input("Enter Centuries: "))
            half = int(input("Enter Half Centuries: "))

            stats = {
                "Matches": matches,
                "Runs": runs,
                "Centuries": centuries,
                "HalfCenturies": half
            }

            players.append((player_id, name, team, stats))
            print("Player registered successfully.")

    elif choice == "2":
        if len(players) == 0:
            print("No players available.")
        else:
            for player in players:
                print("\nPlayer ID      :", player[0])
                print("Player Name    :", player[1])
                print("Team           :", player[2])
                print("Matches        :", player[3]["Matches"])
                print("Runs           :", player[3]["Runs"])
                print("Centuries      :", player[3]["Centuries"])
                print("Half Centuries :", player[3]["HalfCenturies"])
                print("-" * 40)

    elif choice == "3":
        player_id = int(input("Enter Player ID: "))
        found = False

        for player in players:
            if player[0] == player_id:
                found = True
                print("\n1. Matches")
                print("2. Runs")
                print("3. Centuries")
                print("4. Half Centuries")
                ch = input("Enter statistic to update: ")

                if ch == "1":
                    player[3]["Matches"] = int(input("Enter New Matches: "))
                elif ch == "2":
                    player[3]["Runs"] = int(input("Enter New Runs: "))
                elif ch == "3":
                    player[3]["Centuries"] = int(input("Enter New Centuries: "))
                elif ch == "4":
                    player[3]["HalfCenturies"] = int(input("Enter New Half Centuries: "))
                else:
                    print("Invalid choice.")
                    break

                print("Statistics updated successfully.")
                break

        if not found:
            print("Player not found.")

    elif choice == "4":
        player_id = int(input("Enter Player ID: "))
        found = False

        for player in players:
            if player[0] == player_id:
                found = True
                print("\nPlayer ID      :", player[0])
                print("Player Name    :", player[1])
                print("Team           :", player[2])
                print("Matches        :", player[3]["Matches"])
                print("Runs           :", player[3]["Runs"])
                print("Centuries      :", player[3]["Centuries"])
                print("Half Centuries :", player[3]["HalfCenturies"])
                break

        if not found:
            print("Player not found.")

    elif choice == "5":
        if len(players) == 0:
            print("No players available.")
        else:
            highest = players[0]
            for player in players:
                if player[3]["Runs"] > highest[3]["Runs"]:
                    highest = player

            print("\nHighest Run Scorer")
            print("Player Name :", highest[1])
            print("Runs        :", highest[3]["Runs"])

    elif choice == "6":
        found = False
        print()
        for player in players:
            if player[3]["Centuries"] > 10:
                found = True
                print(player[1])
                print("Centuries :", player[3]["Centuries"])
                print()

        if not found:
            print("No player has more than 10 centuries.")

    elif choice == "7":
        if len(players) == 0:
            print("No players available.")
        else:
            teams = {}

            for player in players:
                team = player[2]
                if team in teams:
                    teams[team] += 1
                else:
                    teams[team] = 1

            print()
            for team, count in teams.items():
                print(team, ":", count)

    elif choice == "8":
        print("Thank You")
        break

    else:
        print("Invalid Choice.")