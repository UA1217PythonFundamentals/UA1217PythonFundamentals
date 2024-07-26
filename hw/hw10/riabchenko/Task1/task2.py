class Human:
    species = "Homosapiens"


    def __init__(self, name):
        self.name = name


    def welcome_message(self):
        return f"Welcome, {self.name}"


    @classmethod
    def species_info(cls):
        return f"This is a species of {cls.species}."


    @staticmethod
    def arbitrary_message(name, message):
        return f"{name} is from {message}"


name = input("Enter your Name: ")
arbitrary_message = input("Enter your city: ")


person = Human(name)


print(person.welcome_message())
print(Human.species_info())
print(Human.arbitrary_message(person.name, arbitrary_message))