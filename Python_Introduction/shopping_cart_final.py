"""
    Author: Leonardo Lucas
    Date: 2024-03-24
    Purpose: Create a program that stores a list of products in a shopping cart along with their prices. 
    The user should have to add, remove and compute the price total of the items and display the list.
"""
# Additional Criativity:
# Edit Item and/or their prices
# Implemented try/catch logic
items = []
prices = []

def main():
    print(" \n\n********** Welcome to the shopping cart Program **********")
    while True:
        print("\nPlease select one of the following: \n 1. Add Item \n 2. View Item \n 3. Edit Item \n 4. Remove Item \n 5. Compute Item \n 6. Quit ")
        
        action = input("\nPlease enter an action: ")

        if action == "1":
            add(items, prices)

        elif action == "2":
            view(items, prices)

        elif action == "3":
            edit(items, prices)
        
        elif action == "4":
            remove(items, prices)
        
        elif action == "5":
            compute(prices)
        
        elif action == "6":
            print("\nThank you for using the shopping cart program!")
            break

        else:
            print("\nPlease enter a valid action. (1 to 6)")
            continue

def add(items, prices):
    again = True
    while again:
        item = input("\n What item would you like to add? ").capitalize()
        items.append(item)
        price = float(input(f" What is the price of {item}? $"))
        prices.append(price)
        print(f"\n '{item}' has been added to the cart costing ${price: .2f}.\n")
    
        again = input("\nWould you like to add another item? (y/n): ") == "y" 

    main_menu()   

def view(items, prices):
    print("\n")
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]} - ${prices[i]: .2f}")

def edit(items, prices):
    again = True
    while again:
        view(items, prices)
        try:
            i = int(input("\nWhat item would you like to edit? ")) - 1
            if 0 <= i < len(items):
                new_item = input(f"\nWhat would you like to change {items[i]} to? (Or press Enter to keep it) \n")
                new_price = input(f"What would you like to change {prices[i]} to? (Or press Enter to keep it) \n")

                if new_item:
                    items[i] = new_item
                if new_price:
                    prices[i] = float(new_price)
                
                print(f"Item {i + 1} updated!\n")

            else:
                print("Item does not exist!\n")
                continue
            
            again = input("\nWould you like to edit another item? (y/n): \n") == "y"            

        except ValueError:
            print("That item does not exist in the shopping cart.")

    main_menu()

def remove(items, prices):
    view(items, prices)
    again = True
    while again:
        try:
            i = int(input("\nWhat item would you like to remove? ")) - 1
            if 0 <= i < len(items):
                item_removed = items.pop(i)
                price_removed = prices.pop(i)
                print(f"Item {i + 1}. {item_removed} - ${price_removed} removed!\n")
                view(items, prices)

            else:
                print("Item does not exist!\n")

        except ValueError:
            print("That item does not exist in the shopping cart.")   
      
        again = input("\nWould you like to remove another item? (y/n): \n") == "y"

    main_menu()

def compute(prices):
    total = sum(prices)
    print(f"\nThe total price of the shopping cart is ${total: .2f}.")

    main_menu()

def main_menu(): 
    again = input("\nDo you want to go back to the main menu? (y/n): ") == "y"
    while True:
        if again:
            main()
        else:
            print("\nThank you for using the shopping cart program!")
            break

main()