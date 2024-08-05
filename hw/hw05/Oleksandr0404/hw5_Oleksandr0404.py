# Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.

integers_list = list(range(1, 11))  
list_of_floats = [float(element) for element in integers_list]
print(f'Integers: {integers_list}\n'
      f'Floats: {list_of_floats}\n')

# Print Fibonacci numbers up to the entered number, using cycles.

def print_fibonacci_numbers(user_input):
    try:
      exit_number = int(user_input)
      a, b = 0, 1
      while a <= exit_number:
          print(a, end=' ')
          a, b = b, a + b
      print()
    except:
      print("Error. Enter a valid positive number.")
       
user_input = input("I'll build a Fibonacci sequence for you. Enter the last number: ")
print_fibonacci_numbers(user_input)

# Write a script that will calculate the factorial of the entered number without using recursion. 

def get_factorial(user_input):
   try:
      to_factorial = int(user_input)
      result = 1
      for e in range(1, to_factorial +1):
         result *= e
      print(result)
   except:
     print("Error. Enter a valid positive number.")

user_input = input("Enter a number to find the factorial: ")
get_factorial(user_input)