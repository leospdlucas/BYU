"""
    Author: Leonardo Lucas
    Date: 2024-03-24
    Purpose: Create a program that stores a list of products in a shopping cart along with their prices. 
    The user should have to add and display the list.
"""

shopping_cart =[]

print(" \n********** Welcome to the shopping cart Program! **********\n")
while True:
    print("Please select one of the following: \n 1. Add Item \n 2. View Item \n 3. Quit \n")
    
    action = input("Please enter an action: \n")

    if action == "1":
        item = input("\nWhat item would you like to add? ")
        shopping_cart.append(item)
        print(f" \n{item} has been added to the cart.\n")

    elif action == "2":
        print(f"\n The contents of the shopping cart are: {shopping_cart}")
    
    else:
        print("\nThank you for using the shopping cart program!\n")
        break
   
