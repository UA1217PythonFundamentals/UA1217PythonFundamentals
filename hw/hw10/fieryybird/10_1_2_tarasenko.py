class Human:
  genus = "Homosapiens"

  def __init__(self, name):
    self.name = name

  def welcome(self):
    return f'Welcome, {self.name}.'

  @classmethod
  def message(cls):
    return f'You are {cls.genus}.'
  
  @staticmethod
  def warning():
    return "Don't eat an apple."
  
  
first = Human('Eva')

print(first.welcome())
print(first.message())
print(first.warning())