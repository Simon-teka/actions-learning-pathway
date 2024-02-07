grade_percentage = float(input("Enter your grade percentage: "))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

if grade_percentage >= 70:
    print(f"Congratulations! You passed with a grade of {letter}.")
else:
    print(f"Unfortunately, you did not pass with a grade of {letter}. Better luck next time!")
    
    grade_number = str(letter)  # Convert letter grade to a number for checking + or -
if grade_percentage % 10 >= 7:  # Check if the last digit is >= 7 for a "+"
    sign = "+"
elif grade_percentage % 10 < 3:  # Check if the last digit is < 3 for a "-"
    sign = "-"
else:
    sign = ""  # No sign for the grade

if letter == "A" and grade_percentage >= 97:  # To handle A+ case
    letter = "A+"
    sign = ""
elif letter == "F":  # To handle F+ or F- case
    sign = ""  # No sign for the grade

print(f"Your final grade is {letter}{sign}")