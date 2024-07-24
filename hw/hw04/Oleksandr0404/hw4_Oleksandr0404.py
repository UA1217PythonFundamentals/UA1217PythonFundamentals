def celsium_to_fahrenheit(celsium):
    return (celsium * 9/5) + 32


celsium = float(input("Enter the temperature in Celsium: "))

if celsium < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C).")
else:
    fahrenheit = celsium_to_fahrenheit(celsium)
    print(f"{celsium}°C is equivalent to {fahrenheit:.2f}°F")
