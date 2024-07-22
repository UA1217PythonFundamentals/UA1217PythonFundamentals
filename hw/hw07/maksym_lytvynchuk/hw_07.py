## homework 7.1
     # 1 variant

def numbers(num1, num2):
  """
  The function has 2 parametrs - num1 and num2
  and return a larger number

  """
  if num1 < num2:
    print(num2)
  else:
    print(num1)
    return
  

     # 2 variant

def numbers(num1, num2):
  """
  The function has 2 paramerts - num1 and num2
  The function also return a larger number but contains less code

  """
  return num1 if num1 > num2 else num2

##homework 7.2

def choice():
    def rectangle():
        a = int(input("Enter the a: "))
        b = int(input("Enter the b: "))
        return a * b

    def triangle():
        a = int(input("Enter the a: "))
        h = int(input("Enter the h: "))
        return 0.5 * a * h

    def circle():
        pi = 3.14
        r = int(input("Enter the r: "))
        result = pi * (r ** 2)
        return result

    info = input("Enter your choice :").lower()
    if info == 'rectangle':
        print("Rectangles area = ", rectangle())
    elif info == 'triangle':
        print("Triangles area = ", triangle())
    elif info == 'circle':
        print("Circles area = ", circle())
    else:
        print("Error")

##homework 7.3

def count(word):
   char_count = {}
   for char in word:
      if char in char_count:
         char_count[char] += 1
      else:
         char_count = 1
   return char_count
