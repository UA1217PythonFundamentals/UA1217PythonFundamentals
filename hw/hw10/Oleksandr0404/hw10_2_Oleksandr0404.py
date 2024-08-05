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

# Example usage
person = Human("Bober")

# Instance method
print(person.welcome_message())  # Output: Welcome, Alice!

# Class method
print(Human.species_info())      # Output: Humans are a species of Homosapiens.

# Static method
print(Human.arbitrary_message()) # Output: This is an arbitrary message.
