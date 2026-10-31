members = ["Rahul", "Priya", "Omkar"]
books = ["Python", "AI", "Database"]

authors = {
    "Python": "Guido",
    "AI": "Russell",
    "Database": "Korth"
}

borrowed = {"Omkar": "Database"}


def fol_query():
    predicate = input("Enter predicate: ").strip()
    value = input("Enter value: ").strip()

    if predicate == "Member":
        result = value in members
    elif predicate == "Book":
        result = value in books
    elif predicate == "Available":
        result = value in books and value not in borrowed.values()
    elif predicate == "WrittenBy":
        v = value.split(",")
        result = len(v) == 2 and authors.get(v[0].strip()) == v[1].strip()
    elif predicate == "Borrows":
        v = value.split(",")
        result = len(v) == 2 and borrowed.get(v[0].strip()) == v[1].strip()
    else:
        result = False

    print("TRUE" if result else "FALSE")


def show_kb():
    print("\n--- KNOWLEDGE BASE ---")
    for m in members:
        print("Member(", m, ")")
    for b in books:
        print("Book(", b, ")")
        if b not in borrowed.values():
            print("Available(", b, ")")
    for b, a in authors.items():
        print("WrittenBy(", b, ",", a, ")")
    for m, b in borrowed.items():
        print("Borrows(", m, ",", b, ")")


def add_book():
    b = input("Enter book name: ")
    a = input("Enter author: ")
    if b not in books:
        books.append(b)
        authors[b] = a
        print("Book added")
    else:
        print("Book already exists")


def remove_book():
    b = input("Enter book name: ")
    if b in books and b not in borrowed.values():
        books.remove(b)
        authors.pop(b, None)
        print("Book removed")
    else:
        print("Book not found or currently borrowed")


def borrow_book():
    m = input("Enter member name: ")
    b = input("Enter book name: ")
    if m in members and b in books and b not in borrowed.values():
        borrowed[m] = b
        print("Book borrowed")
    else:
        print("Cannot borrow book")


def return_book():
    m = input("Enter member name: ")
    if m in borrowed:
        print(borrowed.pop(m), "returned")
    else:
        print("No borrowed book found")


while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Check Availability")
    print("6. Find Author")
    print("7. Show Borrowed Books")
    print("8. Display Knowledge Base")
    print("9. Execute FOL Query")
    print("10. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            add_book()

        case "2":
            remove_book()

        case "3":
            borrow_book()

        case "4":
            return_book()

        case "5":
            b = input("Enter book name: ")
            if b in books and b not in borrowed.values():
                print("Book is available")
            else:
                print("Book is not available")

        case "6":
            b = input("Enter book name: ")
            print("Author:", authors.get(b, "Book not found"))

        case "7":
            print("\n--- BORROWED BOOKS ---")
            for m, b in borrowed.items():
                print(m, "borrowed", b)

        case "8":
            show_kb()

        case "9":
            print("\n--- FOL QUERY ---")
            fol_query()

        case "10":
            print("Exiting Library System")
            break

        case _:
            print("Invalid choice")
