class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "Humans are a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

person = Human("Bober")


print(person.welcome_message())  

print(Human.species_info())    

print(Human.arbitrary_message())
