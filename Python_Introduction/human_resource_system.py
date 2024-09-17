"""
    Author: Leonardo Lucas
    Date: 2024-06-03
    Description: Find the overall maximum and minimum life expectancies in the dataset.
"""

# Função para carregar o dataset
def load_dataset(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
    return data, header

# Função para encontrar o valor mínimo e máximo da expectativa de vida no dataset
def find_min_max_life_expectancy(data):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_row = None
    max_row = None
    
    for row in data:
        life_expectancy = float(row[3])
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_row = row
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_row = row
    
    return min_row, max_row

# Função para analisar um ano específico
def analyze_year(data, year):
    year_data = [row for row in data if int(row[2]) == year]
    
    if not year_data:
        print(f"No data available for the year {year}.")
        return
    
    total_life_expectancy = 0
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_row = None
    max_row = None
    
    for row in year_data:
        life_expectancy = float(row[3])
        total_life_expectancy += life_expectancy
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_row = row
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_row = row
    
    avg_life_expectancy = total_life_expectancy / len(year_data)
    
    print(f"For the year {year}:")
    print(f"The average life expectancy across all countries was {avg_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_row[0]} with {max_life_expectancy}")
    print(f"The min life expectancy was in {min_row[0]} with {min_life_expectancy}")

# Caminho do arquivo CSV
file_path = 'life-expectancy.csv'

# Carregar o dataset
data, header = load_dataset(file_path)

# Encontrar o valor mínimo e máximo da expectativa de vida no dataset
min_row, max_row = find_min_max_life_expectancy(data)

print(f"Overall min life expectancy: {min_row[3]} from {min_row[0]} in {min_row[2]}")
print(f"Overall max life expectancy: {max_row[3]} from {max_row[0]} in {max_row[2]}")

# Entrada do usuário para o ano de interesse
year_of_interest = int(input("Enter the year of interest: "))
analyze_year(data, year_of_interest)