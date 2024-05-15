"""Author: Leonarodo Lucas
   Date: 2024-05-15
   Purpose: Write a Guess My Number game
"""

import random
# Implementation of tips for getting thee number right
# Implementation of scores
# Adding my criativity here
print("What is the magic number between 1 and 100. \n Try to guess it in as few attempts as possible. \n The fewer the number of attempts, the higher the score")

number = random.randint(1, 100)
guess = int(input("Take a guess: "))
attempts = 1 # Adding my criativity here
point = 100 # Adding my criativity here
    
while guess != number:
    if guess < number:
        print("Your guess is too low! Take a higher guess")
        
    elif (guess + 10) < number: # Adding my criativity here
        print("Your guess is low! Take a bit higher guess") # Adding my criativity here
    
    elif (guess + 5) < number: # Adding my criativity here
        print("Almost there! You're close to getting it right...") # Adding my criativity here

    elif (guess - 5) > number: # Adding my criativity here
        print("Almost there! You're close to getting it right...") # Adding my criativity here
        
    elif (guess - 10) > number: # Adding my criativity here
        print("Your guess is high! Take a bit lower guess") # Adding my criativity here
    
    else:
        print("Your guess is too high! Take a lower guess")

    guess = int(input("Take a guess: "))
    attempts += 1

point = point - attempts # Adding my criativity here

print(f"Good job! You guessed my number in {str(attempts)} guesses! \n Your score is: {point}") # Adding my criativity here