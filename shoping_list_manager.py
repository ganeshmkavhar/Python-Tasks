# Shopping List Manager

# Initialize an empty list to hold the shopping items
shopping_list = []

# Create a loop to display the menu and handle user input
while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Item added.")

    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == '3':
        print("Shopping List:")
        if shopping_list:
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == '4':
        shopping_list.clear()
        print("Shopping list cleared.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid option. Please choose a valid option.")
