# Converts temperature in Celsius(c) to Fahrenheit(f) 
def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

ABS_ZERO = -273.15
temp_cels = float(input('Enter the temperature in Celsius: '))

if temp_cels > ABS_ZERO: 
    temp_fahr = celsius_to_fahrenheit(temp_cels)
    print(f'{temp_cels}°C is equivalent to {temp_fahr}°F')
else:
    print('Error: Temperature below absolute zero (-273.15°C)')