"""
    Author: Leonardo Lucas
    Date: 2024-06-05
    Description: This program calculates the wind chill based on a given temperature and wind speed. 

"""
# Showing creativity 
# Implemented graphics to show the wind 
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Installing graphics package. . . ")
try:
    import matplotlib.pyplot as plt
except ImportError:
    install('matplotlib')
    import matplotlib.pyplot as plt
print("Package installed!")

def calculate_wind_chill(temp_f, wind_speed):
    """Calculate and return the wind chill based on a given temperature and wind speed."""
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    """Convert from Celsius to Fahrenheit and return the converted temperature."""
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def main():
    # Get the temperature range from the user
    start_temp = float(input("Enter the starting temperature: "))
    end_temp = float(input("Enter the ending temperature: "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Convert the temperatures to Fahrenheit if necessary
    if unit == 'C':
        start_temp = celsius_to_fahrenheit(start_temp)
        end_temp = celsius_to_fahrenheit(end_temp)

    # Generate the list of temperatures in the correct order
    if start_temp > end_temp:
        step = -0.1
    else:
        step = 0.1

    temps = [round(start_temp + i * step, 1) for i in range(int(abs(end_temp - start_temp) / 0.1) + 1)]

    # Display the wind chill for each temperature in the range
    for temp in temps:
        wind_chill_values = []
        wind_speeds = list(range(5, 65, 5))
        for wind_speed in wind_speeds:
            wind_chill = calculate_wind_chill(temp, wind_speed)
            wind_chill_values.append(wind_chill)
            print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

        # Plotting the wind chill values for the current temperature
        plt.plot(wind_speeds, wind_chill_values, label=f"{temp:.1f}F")

    # Configure and show the plot
    plt.title("Wind Chill vs. Wind Speed")
    plt.xlabel("Wind Speed (mph)")
    plt.ylabel("Wind Chill (Fahrenheit)")
    plt.legend(title="Temperatures")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

