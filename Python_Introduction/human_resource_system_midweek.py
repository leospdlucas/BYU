# Step 1: Load the dataset
file_path = 'life-expectancy.csv'

# Variables to store the maximum and minimum life expectancies
max_life_expectancy = float('-inf')
min_life_expectancy = float('inf')

with open(file_path, 'r') as file:
    # Step 2: Read the file line by line
    header = file.readline()  # Skip the header line
    for line in file:
        # Step 3: Split each line into parts
        parts = line.strip().split(',')
        
        # Extract the relevant information
        country = parts[0]
        year = int(parts[1])
        life_expectancy = float(parts[3])
        
        # Step 4: Find the minimum and maximum life expectancies
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
        
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy

# Step 5: Display the results
print(f'The overall max life expectancy is: {max_life_expectancy}')
print(f'The overall min life expectancy is: {min_life_expectancy}')
