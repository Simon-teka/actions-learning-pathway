# Create an empty list to store the names of the items in the shopping cart
shopping_cart = []

# Function to add an item to the shopping cart
def add_item():
    item = input("What item would you like to add? ")
    shopping_cart.append(item)
    print(f"'{item}' has been added to the cart.")

# Function to display the contents of the shopping cart
def display_cart():
    print("The contents of the shopping cart are:")
    for index, item in enumerate(shopping_cart, start=1):
        print(f"{index}. {item}")

# Function to remove an item from the shopping cart
def remove_item():
    display_cart()
    if shopping_cart:
        try:
            item_number = int(input("Which item would you like to remove? ")) - 1
            if 0 <= item_number < len(shopping_cart):
                removed_item = shopping_cart.pop(item_number)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    else:
        print("The shopping cart is already empty.")

# Function to quit the program
def quit_program():
    print("Thank you. Goodbye.")
    exit()

# Main function to display the menu and handle user input
def main():
    while True:
        print("\nWelcome to the Shopping Cart Program!")
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Quit")

        action = input("Please enter an action: ")
        if action == "1":
            add_item()
        elif action == "2":
            display_cart()
        elif action == "3":
            remove_item()
        elif action == "4":
            quit_program()
        else:
            print("Invalid choice. Please enter a valid action.")

# Run the main function
if __name__ == "__main__":
    main()
