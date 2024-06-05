"""
    Author: Leonardo Lucas
    Date: 2024-06-05
    Description: This program calculates the wind chill based on a given temperature and wind speed.

"""

# Showing creativity 
# Implemented to user input a range of temperature
def calculate_wind_chill(temp_f, wind_speed):
    """Calculate and return the wind chill based on a given temperature and wind speed."""
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    """Convert from Celsius to Fahrenheit and return the converted temperature."""
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def main():
    # Showing creativity 
    # Get the temperature range from the user
    start_temp = float(input("Enter the starting temperature: "))
    end_temp = float(input("Enter the ending temperature: "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Convert the temperatures to Fahrenheit if necessary
    if unit == 'C':
        start_temp = celsius_to_fahrenheit(start_temp)
        end_temp = celsius_to_fahrenheit(end_temp)

    # Display the wind chill for each temperature in the range
    for temp in range(int(start_temp), int(end_temp) + 1):
        # Display the wind chill for wind speeds from 5 to 60 mph
        for wind_speed in range(5, 65, 5):
            wind_chill = calculate_wind_chill(temp, wind_speed)
            print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

main()