# Exercise 1: Library Management using Predicate Logic

members = ["Rahul", "Priya", "Omkar"]

books_issued = {
    "Rahul": 4,
    "Priya": 2,
    "Omkar": 1
}

membership_expired = ["Omkar"]


def knowledge_base():
    print("\n--- KNOWLEDGE BASE ---")

    for student in members:
        print("Student(", student, ")")

    for student, count in books_issued.items():
        print("BooksIssued(", student, ",", count, ")")

    for student in membership_expired:
        print("MembershipExpired(", student, ")")


def inference():
    print("\n--- INFERRED CONCLUSIONS ---")

    for student, count in books_issued.items():
        if count > 3:
            print("BorrowingLimitExceeded(", student, ")")

    for student in membership_expired:
        print("BorrowingDenied(", student, ")")


while True:
    print("\n--- LIBRARY MENU ---")
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
