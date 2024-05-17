""" Author: Leonardo Lucas

    Purpose: Calculating the Meal Price regarding the number of adults and children and their prices and others taxes
"""

# ADDITIONAL CREATIVITY: Implementating the possibility for the customer to pay a tip
child_m = float(input("What is the price of a child's meal? $"))
adult_m = float(input("What is the price of a adult's meal? $"))
n_children = int(input("How many children are there? "))
n_adults = int(input("How many adults are there? "))

sub_t = float((child_m * n_children) + (adult_m * n_adults))
print(f"\nSubtotal: ${sub_t: .2f}\n")

sales_tax = float(input("What is the sales tax rate? ")) * sub_t / 100
print(f"Sales Tax: ${sales_tax: .2f}")

# Including the possibility for the customer to pay a tip
tip = input("Would you like to pay the 10% tip? (y or n) ")
if tip == 'y':
    total = sales_tax + (sub_t * 10 / 100) + sub_t
    print(f"Total: ${total}\n")
else:
    total = sales_tax + sub_t
    print(f"Total: ${total}\n")

# Including control structure - While     
payment = float(input("What is the payment amount? $"))
if payment > total:
    change = payment - total
    print(f"Change: ${change: .2f}")
else:
    while payment < total:
        left = total - payment
        print(f"Insufficient value! There are still ${left: .2f} left for full payment.")
        break
