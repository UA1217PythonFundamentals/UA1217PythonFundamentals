special_characters = "! @#$%^&*()+?_=,\\<>/\"'"
ABS_ZERO = -273.15


def celsius_to_fahrenheit(celsius):
  fahrenheit = round((celsius * 9 / 5) + 32, 1)
  return fahrenheit


user_input = input("Enter the temperature in Celcius: ")

if not user_input.isalpha() and not any(char in user_input for char in special_characters):
  temp_celcius = float(user_input)
  if temp_celcius < ABS_ZERO:
    print(f"Error: Temperature below absolute zero ({ABS_ZERO}°C)") 
  else: 
    temp_fahrenheit = celsius_to_fahrenheit(temp_celcius)
    print(f'{temp_celcius}°C is equivalent to {temp_fahrenheit}°F')
else: 
  print("Your input is not a valid number. Don't ruin my program!")

  