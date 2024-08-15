temp_cels = int(input("Enter a temperature Celsius: "))
if temp_cels > (- 273.15): 
    temp_fahr = (temp_cels * 9/5) + 32
    print(f"{temp_cels}°C is equivalent to {temp_fahr}°F")
else:
    print ("Error: Temperature below absolute zero (-273.15C)")