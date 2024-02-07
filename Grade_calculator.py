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