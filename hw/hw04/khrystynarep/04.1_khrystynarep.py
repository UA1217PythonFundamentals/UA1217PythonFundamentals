# prompts the user to enter a temperature in Celsius and then converts it to Fahrenheit
temperature=input('Enter the temperature in Celsius:\n', )
temp=int(temperature)
if temp>(-273.15):
    F=(temp*(9/5))+32
    print(f"{temp}°C is equivalent to {F}°F")
else: 
    print('Error: Temperature below absolute zero (-273.15°C)')