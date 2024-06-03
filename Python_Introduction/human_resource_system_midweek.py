"""
    Author: Leonardo Lucas
    Date: 2024-06-03
    Description: Find the overall maximum and minimum life expectancies in the dataset.
"""

# Criativity Content
# Implemented average life expectancies
# Function to load the dataset
def load(file_path):
    dataset = []
    with open(file_path, 'r') as file: # 'r' read mode
        lines = file.readlines() # Reads all lines of the file and stores them in a list named lines.
        for line in lines[1:]:  # Skip the header row
            row = line.strip().split(',')
            dataset.append(row)
    return dataset

# Function to find the average, lowest and highest life expectancies
def find_min_max_avg_life_expectancy(dataset):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    total_life_expectancy = 0
    num_countries = len(dataset)

    for row in dataset:
        life_expectancy = float(row[2])  # Assuming life expectancy is in the third column
        total_life_expectancy += life_expectancy
        
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
    
    avg_life_expectancy = total_life_expectancy / num_countries

    return min_life_expectancy, max_life_expectancy, avg_life_expectancy

# Main program
def main():
    file_path = 'life-expectancy.csv'
    dataset = load(file_path)
    min_life_expectancy, max_life_expectancy, avg_life_expectancy = find_min_max_avg_life_expectancy(dataset)
    print(f"Lowest life expectancy: {min_life_expectancy: .2f}")
    print(f"Highest life expectancy: {max_life_expectancy: .2f}")
    print(f"Average life expectancy: {avg_life_expectancy: .2f}")

main()