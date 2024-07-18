class Human():
    def __init__(self, name):
        self.name = name
        
    def greet(self):    
        return(f"Hello {self.name}")

    @classmethod
    def info(cls):
        return("This is a Homosapiens.")
    
    @staticmethod
    def static_metod():
        return("Hello everyone")
    

person1 = Human("Andriy")

print(person1.greet())

print(Human.info())

print(Human.static_metod())