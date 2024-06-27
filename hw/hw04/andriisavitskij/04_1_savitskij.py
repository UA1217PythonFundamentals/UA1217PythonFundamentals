temperature=float(input("Enter the temperature: "))
if  temperature < -273.15:
    print("Error. you entered invalid value.")
else:
    fahren=temperature*9/5+32
    print(f"Okay, so: {temperature}°C is equivalent to {fahren}°F")