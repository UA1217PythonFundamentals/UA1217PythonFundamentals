# task 1

# temperature converter

temp = float(input("Enter temperature: "))
F = temp * 9/5 + 32

if temp < -273.15:
    print("Error. Temperature must be > -273.15")
else:
    print(f'{temp}\u00B0C is equivalent {F}\u00B0F')