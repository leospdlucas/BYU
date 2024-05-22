""" 
    Author: Leonardo Lucas
    Date: 2024-05-22
    Purpose: Write a program to show a list of numbers, inputed by the user and output the sum, the average and the maximum or largest of themselves.
    Strech Challenge 1: User can input a negative or positive number and output the smallest positive number
    Strech Challenge 2: Sort the numbers in ascending order
"""
# Additional Criativity:
# Implementing the restart the game or not
def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def average(numbers):
    average = sum(numbers) / len(numbers)
    return average

def largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def sort(numbers):
    sorted_list = sorted(numbers)
    return sorted_list

def main():
    repeat = True
    while repeat:
        print("\n**** This is our list of numbers ****")
        print("\nEnter 0 to stop\n")
        numbers = []
        while True:
            number = int(input("Enter a number: "))
            if number == 0:
                break
            numbers.append(number)

        print(f"\nThe sum of the numbers is {sum(numbers)} ")
        print(f"The average of the numbers is {average(numbers)}")
        print(f"The largest number is {largest(numbers)}")
        print(f"The smallest number is {smallest(numbers)}")
        print(f"The numbers in ascending order are {sort(numbers)}")

        repeat = input(f"Do you want to do other list? (y/n)").lower == "y"
    print("\nThank you for playing the Guess My Number game! \n") 

main()