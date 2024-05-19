"""Author: Leonarodo Lucas
   Date: 2024-05-18
   Purpose: Write a Word Puzzle Game
"""
# Additional Criativity:
# Implementing 'nltk' library (Natural Language ToolKit), which includes a corpus of words for generating random words automatically;
# It was necessary to install the library manually 
# import nltk 
# nltk.download('words')
# Implementing the restart the game or not
# Implementing score
import random
import nltk
from nltk.corpus import words 

# Ensure the NLTK words corpus is downloaded
# Additional Criativity
print("\nInstalling libraries...\n")
nltk.download('words')
print("\nInstallation complete!\n")

def tips(hidden_word, guess, now_tip):
    tip = []
    for i in range(len(hidden_word)):
        if i < len(guess) and guess[i] == hidden_word[i]: 
            tip.append(guess[i].upper())  # letter in the hidden word at same position with capital letter
        elif i < len(guess) and guess[i] in hidden_word:
            tip.append(guess[i].lower())  # letter in the hidden word at different position with lowercase letter
        else:
            tip.append(now_tip[i * 2]) if i * 2 < len(now_tip) else tip.append("_")  # Maintain existing tip or underscore
    return " ".join(tip)  # Return a formatted string containing the hidden word and its corresponding letter 

def game():
    again = True

    while again: # Additional Criativity
        word_list = words.words()  # List of English words from nltk.corpus
        hidden_word = random.choice(word_list).lower()  # Random word from the list
        score = 110

        print("\n******* Welcome to the WORD GUESSING GAME ******* \n")
        print(hidden_word) # Printing the hidden word here because I created a MONSTER!!

        tip = '_ '  * len(hidden_word)
        attempts = 0

        while True:
            print(f"\nThis is your tip:                   {tip.split()}")
            guess = input(f"Guess this word which has {len(hidden_word)} letters: ").lower()
            attempts += 1

            if guess == hidden_word: # Imagine if the dude nails it on the first shot!!!
                print(f"\nCongratulations! You guessed the hidden word in {attempts} attempts!")
                break
            
            if guess in hidden_word:
                tip = tips(hidden_word, guess, tip)  # Pass 'tip' as the third argument
                if tip == hidden_word:
                    print(f"\nCongratulations! You guessed the hidden word in {attempts} attempts!")
                    break
            else:
                print(f"\nSorry, the letter {guess} is not in the word. Try again!")
            
            tip = tips(hidden_word, guess, tip)  

        score -= attempts * 10 # Additional Criativity
        print(f"\nYour score is {score} \n")
        again = input("\nDo you want to play again? (y/n): \n").lower() == "y" # Additional Criativity

    print("\nThank you for playing the WORD GUESSING GAME! \n") 

game()