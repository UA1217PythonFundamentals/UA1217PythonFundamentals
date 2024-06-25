c = float(input("Enter the temperature in Celsius: "))
if c < -273.15:
    print("Temperature below absolute zero (-273.15°С)")
else:
    f = (c * 9/5) + 32
    print(f'{c}°C is equivalent to {f}°F')