# Obtain ratings from the user
loan_size = int(input("Enter the loan size rating (1-10): "))
credit_history = int(input("Enter your credit history rating (1-10): "))
income = int(input("Enter your income rating (1-10): "))
down_payment = int(input("Enter your down payment rating (1-10): "))

# Boolean variable to determine loan decision
loan_decision = False

# Applying the rules to make the loan decision
if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        loan_decision = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            loan_decision = True
        else:
            loan_decision = False
    else:
        loan_decision = False
else:
    if credit_history < 4:
        loan_decision = False
    else:
        if income >= 7 or down_payment >= 7:
            loan_decision = True
        elif income >= 4 and down_payment >= 4:
            loan_decision = True
        else:
            loan_decision = False

# Display the decision to the user
if loan_decision:
    print("Congratulations! You qualify for the loan.")
else:
    print("We regret to inform you that you do not qualify for the loan.")

