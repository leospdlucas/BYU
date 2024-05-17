"""Author: Leonarodo Lucas
   Date: 2024-05-11
   Purpose: Write a text-based adventure game
   """
import random
import math

# ADDITIONAL CREATIVITY: Implementating a Stone, Paper, and Scissors as battle methods
# Implementing functions logic
# Scenario 1
print("Welcome to the world of Pokemom Trainers!\n")
print("This is a text-based adventure game where you, as a Pokemon trainer, encounter wild Pokemon, rivals, and need to make choices to determine if you will be a failed or successful trainer.\n")

p_name = input("What is your name?\n")

print("You were totally into a game of League of Legends in your room, just about to crush your archenemy, Gary, when your mom barges in and yanks the plug from your computer, causing you to lose the match. Beyond furious, you demand to know why she did it. She's fed up and tells you straight: it's time to get a job; you're 19 already, after all. So, with all your know-how and experience.\n")

job = input("What career path are you thinking of? (MARKETING / ADMINISTRATION / TECHNOLOGY / SCIENCE / POKEMON TRAINER)\n\n").lower()
charmander = ["CHARMANDER", "CHARMELEON", "CHARIZARD"]
squirtle = ["SQUIRTLE", "WARTORTLE", "BLASTOISE"]
bulbasaur = ["BULBASAUR", "IVYSAUR", "VENUSAUR"]

if job != "pokemon trainer":
    print("HAHAHA! You don't even have a high school diploma, you've just been playing League of Legends your whole life and you want to pursue a career!? You have no choice; you can only be a POKEMON TRAINER.\n")
    job = 'pokemon trainer'
    print(f"You meet Professor Oak and then he shows you 3 Pokemon to choose your first one: ({charmander[0]} / {squirtle[0]} / {bulbasaur[0]})\n")
else:
    print("OK! Go to Professor Oak's house to select your first Pokemon.")
    job = 'pokemon trainer'
    print(f"You meet Professor Oak and then he shows you 3 Pokemon to choose your first one: ({charmander[0]} / {squirtle[0]} / {bulbasaur[0]})\n")

def start():
    level = 5
    choice = input(f"Which Pokemon do you choose? ({charmander[0]} / {squirtle[0]} / {bulbasaur[0]})\n").lower()

    if choice == "charmander":
        print(f"Congratulations {p_name}! Your {charmander[0]} Lv: {str(level)} is full of life and ready to battle.")
        party = [charmander[0], level]
        print(f"The {party[0].upper()} Lv: {str(level)} were added to your party.")
        scenario2_charmander(party) # Continue to the next scenario
    elif choice == "squirtle":
        print(f"Congratulations {p_name}! Your {squirtle[0]} Lv: {str(level)} is full of life and ready to battle.")
        party = [squirtle[0], level]
        print(f"The {party[0].upper()} Lv: {level} were added to your party.")
        scenario2_squirtle(party) # Continue to the next scenario
    elif choice == "bulbasaur":
        print(f"Congratulations {p_name}! Your {bulbasaur[0]} Lv: {str(level)} is full of life and ready to battle.")
        party = [bulbasaur[0], level]
        print(f"The {party[0].upper()} Lv: {str(level)} were added to your party.")
        scenario2_bulbasaur(party) # Continue to the next scenario
    else:
        print("Are you kidding me? You must choose between CHARMANDER / SQUIRTLE / BULBASAUR")
        start()  # Restart the scenario

def first_battle(party):
    print(f"You and Gary are now in the same room, and you both decide to fight.")
    print("BATTLE NOTES:\n 1. The battles are decided in a best of 3 matches of Rock, Paper, Scissors; \n 2. Win 2 matches to be the winner of the battle; \n 3. At the beginning of the battle, the name of the Pokémon and its level will be displayed. When you win the battle, your Pokémon receives 10% of the opponent's level as an addition to its own level. \n 4. If it's a wild Pokémon, you'll have the option to capture it. \n 5. When you lose, the match restarts. \n\n")

    print(f"You: {party[0].upper()} Lv: {str(party[1])}")

# Stone, Paper and scissor
def user_choice():
    while True:
        u_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if u_choice in ['rock', 'paper', 'scissors']:
            return u_choice
        else:
            print("Invalid choice. Please choose between Rock, Paper, or Scissors.")

def comp_choice():
    # Random choice
    return random.choice(['rock', 'paper', 'scissors'])

def winner(u_choice, comp_choice):
        if u_choice == comp_choice:
            return "It's a tie!"
        elif (u_choice == 'rock' and comp_choice == 'scissors') or \
             (u_choice == 'paper' and comp_choice == 'rock') or \
             (u_choice == 'scissors' and comp_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

def battle():
    user_score = 0
    comp_score = 0
    print("This is the Rock, Paper, Scissors!")
    while user_score < 2 and comp_score < 2:
        user_choice_b = user_choice()
        comp_choice_b = comp_choice()
        print(f"You chose: {user_choice_b}")
        print(f"The Gary chose: {comp_choice_b}")
        result = winner(user_choice_b, comp_choice_b)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            comp_score += 1
        print(f"Your score: {user_score} | Gary score: {comp_score}")
    if user_score > comp_score:
        print(f"Congratulations {p_name}! You won the battle!")
    else:
        print(f"Gary won the battle! Play again")

print("Right after you chose your starter Pokémon, another person enters the laboratory and introduces themselves as Gary, saying they'll start their journey and want a starter Pokémon, just like you.\nSurprised to meet your League of Legends rival in person, even more so when you find out him live in the same neighborhood as you.\n")

def scenario2_charmander(party):

    print(f"Gary asked Professor Oak for a Charmander but got angry after knowing that you, {p_name}, had already chosen it just minutes before. At that moment, Gary was thinking the same thing as you. 'WE'LL BE RIVALS IN THIS TOO!!!' That's why Gary chose a Pokemon that, naturally, is also a rival to yours... {squirtle[0]}!!!\n")

    party_rival = [squirtle[0], 5]

    first_battle(party)
    print(f"Gary: {party_rival[0].upper()} Lv: {str(party_rival[1])}\n")
    battle_result = battle() # Start the game

    if battle_result ==  "You win!":
        party[1] = math.ceil(party[1] * 1.1)
        print(f"Your {party[0].upper()} leveled up to Lv: {str(party[1])}\n")

    scenario3_charmander()

def scenario2_squirtle(party):

    print(f"Gary asked Professor Oak for a Squirtle but got angry after knowing that you, {p_name}, had already chosen it just minutes before. At that moment, Gary was thinking the same thing as you. 'WE'LL BE RIVALS IN THIS TOO!!!' That's why Gary chose a Pokemon that, naturally, is also a rival to yours... {bulbasaur[0]}!!!\n")

    party_rival = [bulbasaur[0], 5]

    first_battle(party)
    print(f"Gary: {party_rival[0].upper()} Lv: {str(party_rival[1])}\n")
    battle_result = battle() # Start the game

    if battle_result ==  "You win!":
        party[1] = math.ceil(party[1] * 1.1)
        print(f"Your {party[0].upper()} leveled up to Lv: {str(party[1])}\n")

    scenario3_squirtle()

def scenario2_bulbasaur(party):

    print(f"Gary asked Professor Oak for a Bulbasaur but got angry after knowing that you, {p_name}, had already chosen it just minutes before. At that moment, Gary was thinking the same thing as you. 'WE'LL BE RIVALS IN THIS TOO!!!' That's why Gary chose a Pokemon that, naturally, is also a rival to yours... {charmander[0]}!!!\n")

    party_rival = [charmander[0], 5]

    first_battle(party)
    print(f"Gary: {party_rival[0].upper()} Lv: {str(party_rival[1])}\n")
    battle_result = battle() # Start the game

    if battle_result ==  "You win!":
        party[1] = math.ceil(party[1] * 1.1)
        print(f"Your {party[0].upper()} leveled up to Lv: {str(party[1])}\n")

    scenario3_bulbasaur()

def scenario3_charmander():
    print("I really got lazy to build the rest, but we already have the 3 scenarios...\nTHANKS!")

def scenario3_squirtle():
    print("I really got lazy to build the rest, but we already have the 3 scenarios...\nTHANKS!")

def scenario3_bulbasaur():
    print("I really got lazy to build the rest, but we already have the 3 scenarios...\nTHANKS!")

start()