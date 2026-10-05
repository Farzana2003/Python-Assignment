items = []

while True:
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        items.append(item)

    elif choice == "2":
        item = input("Enter an item to remove: ")

        if item in items:
            items.remove(item)
        else:
            print("Item not found")

    elif choice == "3":
        print("Current list:", items)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")