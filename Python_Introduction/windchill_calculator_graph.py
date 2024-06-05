"""
    Author: Leonardo Lucas
    Date: 2024-06-05
    Description: This program calculates the wind chill based on a given temperature and wind speed. 

"""
# Showing creativity 
# Implemented graphics to show the wind 
import matplotlib.pyplot as plt

def calculate_wind_chill(temp_f, wind_speed):
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def main():
    temp = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Convert the temperature to Fahrenheit if necessary
    if unit == 'C':
        temp = celsius_to_fahrenheit(temp)
    
    wind_speeds = list(range(5, 65, 5))
    wind_chill_values = []

    # Calculate wind chill for each wind speed
    for wind_speed in wind_speeds:
        wind_chill = calculate_wind_chill(temp, wind_speed)
        wind_chill_values.append(wind_chill)
        
    # Showing creativity 
    # Plotting
    plt.plot(wind_speeds, wind_chill_values, marker='o', linestyle='-')
    plt.title("Wind Chill vs. Wind Speed")
    plt.xlabel("Wind Speed (mph)")
    plt.ylabel("Wind Chill (Fahrenheit)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
