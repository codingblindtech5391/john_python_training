# Classes Example

# Define a simple class
class Dog:
    # Class variable
    species = "Canis familiaris"

    # Constructor method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print("Woof!")

    # Instance method with formatting
    def get_description(self):
        return f"{self.name} is {self.age} years old."

# Create instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing instance variables
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")

# Accessing class variable
print(f"They both belong to the species: {Dog.species}")

# Calling instance method
dog1.bark()

# Using a method to get a description
print(dog2.get_description())
