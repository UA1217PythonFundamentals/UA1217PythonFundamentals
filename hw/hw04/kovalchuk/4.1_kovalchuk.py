# Task1. "Temperature Converter"

temperature = float(input("Enter the temperature in Celsius:"))

if temperature > (-273.15):
    fahrenheit = (temperature* 9/5) + 32
    print("Fahrenheit temperature:", fahrenheit)
else:
    print("Temperature below absolute zero (-273.15°C)")

