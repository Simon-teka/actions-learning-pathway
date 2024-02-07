# Shopping Cart Program with Additional Features

# Creating an empty list to store the items and their prices in the shopping cart
shopping_cart_items = []
shopping_cart_prices = []

# Function to add an item and its price to the shopping cart
def add_item():
   item = input("What item would you like to add? ")
   price = float(input(f"What is the price of '{item}'? "))
   shopping_cart_items.append(item)
   shopping_cart_prices.append(price)
   print(f"'{item}' has been added to the cart.")

# Function to display the contents of the shopping cart including the prices
def display_cart():
   print("The contents of the shopping cart are:")
   for index, (item, price) in enumerate(zip(shopping_cart_items, shopping_cart_prices), start=1):
       print(f"{index}. {item} - ${price:.2f}")

# Function to compute the total price of the items in the shopping cart
def compute_total():
   total_price = sum(shopping_cart_prices)
   print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

# Function to remove an item from the shopping cart
def remove_item():
   display_cart()
   if shopping_cart_items:
       try:
           item_number = int(input("Which item would you like to remove? ")) - 1
           if 0 <= item_number < len(shopping_cart_items):
               removed_item = shopping_cart_items.pop(item_number)
               removed_price = shopping_cart_prices.pop(item_number)
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
       print("4. Compute total")
       print("5. Quit")

       action = input("Please enter an action: ")
       if action == "1":
           add_item()
       elif action == "2":
           display_cart()
       elif action == "3":
           remove_item()
       elif action == "4":
           compute_total()
       elif action == "5":
           quit_program()
       else:
           print("Invalid choice. Please enter a valid action.")

# Run the main function
if __name__ == "__main__":
   main()
