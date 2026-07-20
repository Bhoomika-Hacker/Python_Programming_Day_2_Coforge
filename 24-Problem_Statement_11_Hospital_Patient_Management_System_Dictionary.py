patients = [
    {
        "PatientId": 101,
        "PatientName": "Aman Verma",
        "Age": 35,
        "City": "Noida",
        "Visits": [
            {
                "VisitId": 1,
                "DoctorName": "Dr. Mehta",
                "Department": "Cardiology",
                "ConsultationFee": 1200,
                "MedicinesCost": 800,
                "Status": "Completed"
            },
            {
                "VisitId": 2,
                "DoctorName": "Dr. Sharma",
                "Department": "General Medicine",
                "ConsultationFee": 700,
                "MedicinesCost": 500,
                "Status": "Pending"
            }
        ]
    },
    {
        "PatientId": 102,
        "PatientName": "Riya Singh",
        "Age": 28,
        "City": "Delhi",
        "Visits": [
            {
                "VisitId": 1,
                "DoctorName": "Dr. Kapoor",
                "Department": "Orthopaedics",
                "ConsultationFee": 1000,
                "MedicinesCost": 650,
                "Status": "Completed"
            }
        ]
    }
]

while True:
    print("\n" + "=" * 70)
    print("              HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=" * 70)
    print("1. Add a New Patient")
    print("2. Add a Medical Visit")
    print("3. View All Patients")
    print("4. Search Patient by ID")
    print("5. Update Visit Status")
    print("6. Calculate Total Medical Bill")
    print("7. Display Patients with Multiple Visits")
    print("8. Display Department-wise Visit Count")
    print("9. Find Patient with Highest Medical Bill")
    print("10. Remove a Visit Record")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = int(input("Enter Patient ID: "))
        found = False
        for p in patients:
            if p["PatientId"] == pid:
                found = True
                break
        if found:
            print("Patient ID already exists.")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            if age <= 0:
                print("Invalid Age.")
            else:
                city = input("Enter City: ")
                patients.append({
                    "PatientId": pid,
                    "PatientName": name,
                    "Age": age,
                    "City": city,
                    "Visits": []
                })
                print("Patient Added Successfully.")

    elif choice == "2":
        pid = int(input("Enter Patient ID: "))
        patient = None
        for p in patients:
            if p["PatientId"] == pid:
                patient = p
                break

        if patient is None:
            print("Patient not found.")
        else:
            vid = int(input("Enter Visit ID: "))
            duplicate = False
            for v in patient["Visits"]:
                if v["VisitId"] == vid:
                    duplicate = True
                    break
            if duplicate:
                print("Visit ID already exists.")
            else:
                doctor = input("Enter Doctor Name: ")
                dept = input("Enter Department: ")
                fee = float(input("Enter Consultation Fee: "))
                med = float(input("Enter Medicines Cost: "))
                if fee < 0 or med < 0:
                    print("Invalid Amount.")
                else:
                    status = input("Enter Status: ")
                    patient["Visits"].append({
                        "VisitId": vid,
                        "DoctorName": doctor,
                        "Department": dept,
                        "ConsultationFee": fee,
                        "MedicinesCost": med,
                        "Status": status
                    })
                    print("Visit Added Successfully.")

    elif choice == "3":
        for p in patients:
            print("\nPatient ID   :", p["PatientId"])
            print("Patient Name :", p["PatientName"])
            print("Age          :", p["Age"])
            print("City         :", p["City"])

            if len(p["Visits"]) == 0:
                print("No Visit Records")
            else:
                for v in p["Visits"]:
                    print("\nVisit ID          :", v["VisitId"])
                    print("Doctor Name       :", v["DoctorName"])
                    print("Department        :", v["Department"])
                    print("Consultation Fee  :", v["ConsultationFee"])
                    print("Medicines Cost    :", v["MedicinesCost"])
                    print("Status            :", v["Status"])
                    print("-" * 40)

    elif choice == "4":
        pid = int(input("Enter Patient ID: "))
        patient = None
        for p in patients:
            if p["PatientId"] == pid:
                patient = p
                break

        if patient is None:
            print("Patient not found.")
        else:
            print("Patient ID   :", patient["PatientId"])
            print("Patient Name :", patient["PatientName"])
            print("Age          :", patient["Age"])
            print("City         :", patient["City"])
            print("Total Visits :", len(patient["Visits"]))

            for v in patient["Visits"]:
                print("\nVisit ID          :", v["VisitId"])
                print("Doctor Name       :", v["DoctorName"])
                print("Department        :", v["Department"])
                print("Consultation Fee  :", v["ConsultationFee"])
                print("Medicines Cost    :", v["MedicinesCost"])
                print("Status            :", v["Status"])
                print("-" * 40)

    elif choice == "5":
        pid = int(input("Enter Patient ID: "))
        vid = int(input("Enter Visit ID: "))
        status = input("Enter New Status: ")

        updated = False

        for p in patients:
            if p["PatientId"] == pid:
                for v in p["Visits"]:
                    if v["VisitId"] == vid:
                        v["Status"] = status
                        updated = True
                        break

        if updated:
            print("Visit Status Updated.")
        else:
            print("Patient or Visit not found.")

    elif choice == "6":
        pid = int(input("Enter Patient ID: "))
        patient = None

        for p in patients:
            if p["PatientId"] == pid:
                patient = p
                break

        if patient is None:
            print("Patient not found.")
        else:
            total = 0
            for v in patient["Visits"]:
                bill = v["ConsultationFee"] + v["MedicinesCost"]
                total += bill
                print("Visit", v["VisitId"], "Bill : ₹", bill)
            print("-" * 30)
            print("Total Bill : ₹", total)

    elif choice == "7":
        found = False
        for p in patients:
            if len(p["Visits"]) > 2:
                found = True
                print("Patient ID :", p["PatientId"])
                print("Patient Name :", p["PatientName"])
                print("Number of Visits :", len(p["Visits"]))
                print("-" * 30)
        if not found:
            print("No Patient has more than two visits.")

    elif choice == "8":
        count = {}
        for p in patients:
            for v in p["Visits"]:
                dept = v["Department"]
                if dept in count:
                    count[dept] += 1
                else:
                    count[dept] = 1

        for d in count:
            print(d, ":", count[d])

    elif choice == "9":
        highest = -1
        patient = None

        for p in patients:
            total = 0
            for v in p["Visits"]:
                total += v["ConsultationFee"] + v["MedicinesCost"]
            if total > highest:
                highest = total
                patient = p

        if patient is not None:
            print("Patient with Highest Medical Bill")
            print("Patient ID :", patient["PatientId"])
            print("Patient Name :", patient["PatientName"])
            print("Total Bill : ₹", highest)

    elif choice == "10":
        pid = int(input("Enter Patient ID: "))
        vid = int(input("Enter Visit ID: "))

        patient = None

        for p in patients:
            if p["PatientId"] == pid:
                patient = p
                break

        if patient is None:
            print("Patient not found.")
        else:
            removed = False
            for v in patient["Visits"]:
                if v["VisitId"] == vid:
                    patient["Visits"].remove(v)
                    removed = True
                    break

            if removed:
                print("Visit Removed Successfully.")
            else:
                print("Visit not found.")

    elif choice == "11":
        print("Thank You")
        break

    else:
        print("Invalid Choice.")