temp = int(input("Enter the temperature in Celsius: " )) 
if temp > -273.15:
    f = (temp * 9/5) + 32
    print(f"{temp}°C is equivalent to {f}°F ")
else:
    print("Error: The temperature is below absolute zero (-273.15°C)")
