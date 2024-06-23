#the user enters a temperature in Celsius
celsius_temperature = float(input("Enter a temperature in Celsius: "))
#variable for temperature validation
ERROR_TEMPERATURE = -273.15

#print converted vavue if it matched the condition
if celsius_temperature >= ERROR_TEMPERATURE:
    # converting °C into °F
    fahrenheit_temperature = (celsius_temperature * 9 / 5 + 32)
    print(f"{celsius_temperature}°C equals {fahrenheit_temperature}°F")
#print validation message if it didn't match the condition
else:
    print("The entered value can not be below absolute zero (-273.15°C)")