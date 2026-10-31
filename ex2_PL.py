# Exercise 2: Hospital Management using Predicate Logic

patients = ["Amit", "Riya", "Suresh"]

fever = ["Amit", "Suresh"]
cough = ["Amit", "Riya"]
insurance = ["Amit", "Suresh"]

age = {
    "Amit": 45,
    "Riya": 25,
    "Suresh": 68
}


def knowledge_base():
    print("\n--- KNOWLEDGE BASE ---")

    for p in patients:
        print("Patient(", p, ")")

    for p in fever:
        print("Fever(", p, ")")

    for p in cough:
        print("Cough(", p, ")")

    for p in insurance:
        print("Insurance(", p, ")")

    for p, a in age.items():
        print("Age(", p, ",", a, ")")


def inference():
    print("\n--- INFERRED CONCLUSIONS ---")

    for p in patients:

        # Rule 1: Fever and Cough -> Flu
        if p in fever and p in cough:
            print("Flu(", p, ")")

        # Rule 2: Insurance -> CashlessTreatment
        if p in insurance:
            print("CashlessTreatment(", p, ")")

        # Rule 3: Age > 60 -> SeniorCitizen
        if age[p] > 60:
            print("SeniorCitizen(", p, ")")

            # Rule 4: SeniorCitizen and Insurance -> PriorityTreatment
            if p in insurance:
                print("PriorityTreatment(", p, ")")


while True:
    print("\n--- HOSPITAL MENU ---")
    print("1. Display Knowledge Base")
    print("2. Apply Inference Rules")
    print("3. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            knowledge_base()

        case "2":
            inference()

        case "3":
            print("Exiting")
            break

        case _:
            print("Invalid choice")
