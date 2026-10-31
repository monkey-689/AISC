
student = input("Enter Student Name: ")
book = input("Enter Book Name: ")

issued = input("Is the book issued? (yes/no): ").lower()
late = int(input("Enter Number of Late Days: "))
reserved = input("Is the book reserved? (yes/no): ").lower()
membership = input("Is Membership Active? (yes/no): ").lower()
paid = input("Has Fine been Paid? (yes/no): ").lower()

print("\n========== FACTS ==========")

print(f"Student({student})")

if issued == "yes":
    print(f"Issued({student}, {book})")

print(f"DaysLate({student}, {late})")

if reserved == "yes":
    print(f"Reserved({book})")

if membership == "yes":
    print(f"MembershipActive({student})")

if paid == "yes":
    print(f"FinePaid({student})")


print("\n========== INFERENCE ==========")

if issued == "yes":
    print(f"Borrower({student})")

if late > 0:
    print(f"Fine({student})")

if reserved == "yes":
    print(f"BookUnavailable({book})")

if membership == "yes" and paid == "yes":
    print(f"CanBorrowAgain({student})")
else:
    print(f"{student} must pay the fine or activate membership before borrowing again.")
