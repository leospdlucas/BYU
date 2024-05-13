""" The code below contains the stretching challenge and my additional creativity, replacing the if-elif-else blocks, simulating a switch logic, by the switcher dictionary, including functions concepts.
"""

grade = int(input("Enter your grade (0 to 100): "))
# def: defining a function
# grade: argument to
# the switcher dictionary
# lambda function to recieve two arguments as a anonymous function, the grade inputed and the grade determined
def set_letter_grade(grade):
    switcher = { 
        lambda letter_grade: letter_grade >= 90: 'A', 
        lambda letter_grade: letter_grade >= 80: 'B',
        lambda letter_grade: letter_grade >= 70: 'C',
        lambda letter_grade: letter_grade >= 60: 'D',
        lambda letter_grade: letter_grade < 60: 'F'
    } 

    # This loop walks over each item (lambda letter_grade), that represents a condition and the value is the corresponding letter_grade
    for condition, letter in switcher.items():
        if condition(grade):
            return letter
    return None

# Stretch challenge 1
def set_sign(grade):
    last_digit = int(str(grade)[-1]) # Tranforming to string to manipulate it and take the last digit
    print(last_digit)
    if last_digit >= 7:
        return '+'
    elif last_digit < 3:
        return '-'
    else:
        return ''

# letter recieve the function
letter = set_letter_grade(grade)

# Idem for the sign
sign = set_sign(grade)

# Stretch Challenge 3
if letter == 'A' and sign == '+':
    letter = 'A'
    sign = ''

elif letter == 'F' and (sign == '+' or sign == '-'):
    sign = ''

if letter and letter >= 'C':
    print("Congratulations! You passed the course with a grade of", letter + sign)
else:
    print("That's not the Game Over! You could continue this course and try again")

print("Your letter grade is:", letter + sign if letter else "Invalid")