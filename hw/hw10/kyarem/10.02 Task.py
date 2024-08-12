#Task2. Create a class Human, everyone has a name, create a method in the
#class that displays a welcome message to each person. Create a class method
#in the class that returns information that it is a species of "Homosapiens". And
#in the class create a static method that returns an arbitrary message.


class Human:
    name = None
    species_1 = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return cls.species_1

    @staticmethod
    def random_message():
        return "Some message"

human1 = Human("Khrystyna")
human1.welcome_message()
print(Human.species())
print(Human.random_message())