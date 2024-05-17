"""Author: Leonarodo Lucas
   Date: 2024-05-15
   Purpose: Write a Guess My Number game
"""

import random
# Implementation of tips for getting thee number right
# Implementation of scores
# Adding my criativity here
def main():
    print("Welcome to the Guess My Number game! \n")
    print("What is the magic number between 1 and 100. \n Try to guess it in as few attempts as possible. \n The fewer the number of attempts, the higher the score. \n")

    repeat = True

    while repeat:
        number = random.randint(1, 100)
        guess = int(input("Take a guess: "))
        attempts = 1 
        point = 105 # Adding my criativity here

        while guess != number:
            if abs(guess - number) <= 10 and abs(guess - number) > 5: # Adding my criativity here
                if guess < number:
                    print("Your guess is LOW! Take a bit higher guess \n") # Adding my criativity here
                else:
                    print("Your guess is HIGH! Take a bit lower guess \n") # Adding my criativity here

            elif abs(guess - number) <=5: # Adding my criativity here
                if guess < number:
                    print("Almost there! You're close to getting it right... Little HIGH \n") # Adding my criativity here
                else:
                    print("Almost there! You're close to getting it right... Little LOW \n") # Adding my criativity here

            elif guess < number:
                print("Your guess is too LOW! Take a higher guess \n")
            
            else:
                print("Your guess is too HIGH! Take a lower guess \n")
            
            guess = int(input("\nTake a guess: "))
            attempts += 1

        point -= attempts * 5 # Adding my criativity here

        # Strech Challenge 1
        print(f"Good job! You guessed my number in {str(attempts)} guesses! \n Your score is: {str(point)} \n") # Adding my criativity here

        # Strech Challenge 2 boolean
        repeat = input(f"Do you want to play again? (y/n): \n").lower() == "y"
    
    print("\nThank you for playing the Guess My Number game! \n") 

main()