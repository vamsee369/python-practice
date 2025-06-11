phonebook = {}

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        search_name = input("Enter name to search: ")
        print("Phone number:", phonebook.get(search_name, "Not found"))

    elif choice == "3":
        print("Exiting Phonebook. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
