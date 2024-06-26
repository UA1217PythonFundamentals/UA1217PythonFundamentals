C_temp = float(input("Enter the temperature in Celsius: "))
if C_temp < -273.15 :
    print("Error: Temperature below absolute zero (-273.15°C)")
else :
    F_temp = C_temp * (9/5) + 32
    print(f"{C_temp}°C is equivalent {F_temp}°F")