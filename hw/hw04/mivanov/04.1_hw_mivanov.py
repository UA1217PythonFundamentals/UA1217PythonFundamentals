Celcius_temp = input("\nEnter a temperature in Celcius: ")
abs_zero = -273.15
spec_chars = "[@_, -=!#$%^&*()<>?/\\|}{~:]"

if Celcius_temp.isalpha() or (any(char in Celcius_temp for char in spec_chars) and Celcius_temp[0]!="-"):
    print("You input incorrect info. Please, try again.")
elif Celcius_temp[0]=="-" or Celcius_temp.isdigit:
    if float(Celcius_temp) >= abs_zero:
        Fahrenheit_temp = round((float(Celcius_temp)*(9/5)+32), 2)
        print(f"{Celcius_temp}°C is equivalent to {Fahrenheit_temp}°F.")
    else:
        print("Error: Temperature below absolute zero (-273.15°C)")