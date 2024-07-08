temp = int(input("Enter the temparature in Celsium :"))
if temp < -273.15:
    print("Error. Temperature below absolute zero(-273.15°C)")
else:
    degree_sign = u"\N{DEGREE SIGN}"
    F = (temp*9/5)+32
    print(f"{F}{degree_sign}F", "is equivalent", f"{temp}{degree_sign}C")