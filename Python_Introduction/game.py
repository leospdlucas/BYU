"""Author: Leonarodo Lucas
   Date: 2024-05-11
   Purpose: Write a text-based adventure game
   """
print('This is a text-based adventure game where you, as an pokemon trainer, encounter wild pokemons, rivals and need to make choices to determine if you will be a failed ou successful trainer.')

p_name = input("What is your name? ")

print("You were totally into a game of League of Legends in your room, just about to crush your archenemy, Gary, when your mom barges in and yanks the plug from your computer, causing you to lose the match. Beyond furious, you demand to know why she did it. She's fed up and tells you straight: it's time to get a job; you're 19 already, after all. So, with all your know-how and experience")

choice = input("what career path are you thinking of? (MARKETING / ADMINISTRATION / TECHNOLOGY / SCIENCE / POKEMOM TRAINER)\n").lower()

if choice != "pokemom trainer":
   print("HAHAHA! You don't even have a high school diploma, you've just been playing League of Legends your whole life and you want to pursue a career!?. You only could be a POKEMOM TRAINER. ")
else:
   print("OK! Go to Prof. Oak's house to select your first pokemom. ")
   choice = 'pokemom trainer'
   

# Scenario 1
def scenario_1():
    

    if choice == "red":
        print("You open the red door and find yourself in a dark hallway.")
        # Continue to the next scenario
        scenario_2_red()
    elif choice == "blue":
        print("You open the blue door and are greeted by sunlight.")
        # Continue to the next scenario
        scenario_2_blue()
    else:
        print("Invalid choice. Please choose between RED or BLUE.")
        scenario_1()  # Restart the scenario

# Scenario 2 (continuation of the red door)
def scenario_2_red():
    print("You follow the hallway and find a staircase leading down to a basement.")
    choice = input("Do you go down the stairs? (YES/NO)\n").lower()

    if choice == "yes":
        print("Upon reaching the basement, you see a table with a key.")
        # Continue to the next scenario
        scenario_3_red()
    elif choice == "no":
        print("You decide not to go down the stairs and return to the hallway.")
        # Continue to the next scenario
        scenario_3_red_no()
    else:
        print("Invalid choice. Please choose between YES or NO.")
        scenario_2_red()  # Restart the scenario

# Scenario 2 (continuation of the blue door)
def scenario_2_blue():
    print("You are outside the cabin. In front of you, there's a trail leading into the forest.")
    choice = input("Do you follow the trail? (YES/NO)\n").lower()

    if choice == "yes":
        print("You follow the trail and venture deeper into the forest.")
        # Continue to the next scenario
        scenario_3_blue()
    elif choice == "no":
        print("You decide not to follow the trail and explore the surroundings of the cabin.")
        # Continue to the next scenario
        scenario_3_blue_no()
    else:
        print("Invalid choice. Please choose between YES or NO.")
        scenario_2_blue()  # Restart the scenario

# Scenario 3 (continuation of the basement, red door)
def scenario_3_red():
    print("You grab the key and return to the hallway.")
    # Continue with more story branching...

# Scenario 3 (continuation of not grabbing the key, red door)
def scenario_3_red_no():
    print("You're back in the hallway.")
    # Continue with more story branching...

# Scenario 3 (continuation of the trail, blue door)
def scenario_3_blue():
    print("You stumble upon a magnificent waterfall.")
    # Continue with more story branching...

# Scenario 3 (continuation of exploring, blue door)
def scenario_3_blue_no():
    print("You find an old abandoned cabin.")
    # Continue with more story branching...

# Start of the game
scenario_1()