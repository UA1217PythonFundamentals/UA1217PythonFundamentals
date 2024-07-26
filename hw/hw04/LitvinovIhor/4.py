celsius = float(input("Enter the temperature in Celsius: "))

# Checking that the temperature is not below absolute zero
if celsius < -273.15:
    print("Error: temperature below absolute zero (-273.15°C)")
else:
    # Fahrenheit conversion
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C corresponds {fahrenheit}°F")