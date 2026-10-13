# 1. Start with an empty list.
shopping_list = []

print("Welcome to the Shopping List Manager!")

while True:
    # 2. Use a loop to show a small menu again and again.
    print("\nMenu:")
    print("add / remove / show / done")
    action = input("Enter action: ").lower().strip()

    if action == "add":
        # Ask for the item and append() it.
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to the list.")

    elif action == "remove":
        # Ask for the item. Check it is actually in the list with 'in'
        # before removing; otherwise print the error message.
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        # Print every item on its own line.
        if len(shopping_list) == 0:
            print("Your list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print("-", item)

    elif action == "done":
        # End the loop with a goodbye message.
        print("Goodbye! Happy shopping.")
        break

    else:
        # Handle invalid menu input gracefully.
        print("Invalid action. Please type add, remove, show, or done.")