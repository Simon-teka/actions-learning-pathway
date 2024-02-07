# Ask the user for the price of a child's meal and store it as a floating point number
child_meal_price = float(input("What is the price of a child's meal? "))

# Ask the user for the price of an adult's meal and store it as a floating point number
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask the user for the number of children and store it as an integer
num_children = int(input("How many children are there? "))

# Ask the user for the number of adults and store it as an integer
num_adults = int(input("How many adults are there? "))

# Compute the subtotal
subtotal = (num_children * child_meal_price) + (num_adults * adult_meal_price)

# Display the subtotal
print(f"Subtotal: ${subtotal:.2f}")

# Ask the user for the sales tax rate and store it as a floating point number
sales_tax_rate = float(input("What is the sales tax rate? "))

# Compute and display the sales tax
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute and display the total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Ask the user for the payment amount and store it as a floating point number
payment_amount = float(input("What is the payment amount? "))

# Compute and display the change
change = payment_amount - total
print(f"Change: ${change:.2f}")

# Calculate and display the average cost per person
average_cost_per_person = total / (num_children + num_adults)
print(f"Average Per Person: ${average_cost_per_person:.2f}")