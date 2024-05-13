"""Author: Leonardo Lucas
   Date: 2024-05-11
   Purpose: Write a program that determines the letter for a course
"""

grade = int(input("Enter your grade (0 to 100): "))
if grade >= 90:
    letter = "A"

elif grade >= 80:
    letter = "B"

elif grade >= 70:
    letter = "C"

elif grade >= 60:
    letter = "D"

else:
    letter = "F"

# Stretch Challenge 1
sign = ""
tenth = int(str(grade)[-1])
if tenth >= 7:
    sign = '+'

elif tenth < 3:
    sign = '-'

else:
    sign = ""

# Stretch challenge 2 and 3
if letter == "F" or grade >= 93:
    sign = ""

print(f"Your letter grade is: {letter} {sign}")

if grade >= 70:
    print("Congratulations, you passed the course!")
else:
    print("That's not the Game Over! You could continue this course and try again")