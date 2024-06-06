"""
    Author: Leonardo Lucas
    Date: 2024-06-05
    Description: This program calculates the wind chill based on a given temperature and wind speed. 
"""

# Showing creativity: Try and catch errors
# Calculate and return the wind chill based on a given temperature and wind speed.
def calculate_wind_chill(temp_f, wind_speed):

# Calculate the wind chill based on temperature (F) and wind speed (mph).
# Formula: Wind Chill = 35.74 + 0.6215 * T - 35.75 * V^0.16 + 0.4275 * T * V^0.16
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return round(wind_chill, 2)

def celsius_to_fahrenheit(temp_c):
# Convert temperature from Celsius to Fahrenheit.
# Formula: F = C * (9/5) + 32
    temp_c * (9 / 5) + 32

    return temp_c

def main():
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)

    print(f"At temperature {temperature:.1f}F:")
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

main()
