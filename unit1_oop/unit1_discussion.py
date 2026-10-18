"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable. ***
# - Include at least two instance variables. ***
# - Include a constructor (__init__). ***
# - Include a method that returns or displays information about the object. ***
#
# Replace the pass statement with your implementation. ***

class Animal:
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old! Alive: {self.is_alive}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable. ***
# - Add at least two new instance variables. ***
# - Add at least one new method. ***
# - Override a method from the parent class. ***
#
# Replace the pass statement with your implementation. ***

class Dog(Animal):
    species = "dog"

    def __init__(self, name, age, breed, is_trained):
        super().__init__(name, age)
        self.breed = breed
        self.is_trained = is_trained

    def bark(self):
        return f"{self.name} is barking! Woof woof!"

    def get_info(self):
        trained = "trained" if self.is_trained else "not trained"
        return f"{self.name} is a {self.is_trained} {self.age} year old {self.species} with the breed of {self.breed}! Alive: {self.is_alive}"



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class. **
# - Access a class variable through the class itself. **
# - Access the same class variable through an object. **
# - Add a new attribute to only one object after it is created. **
# - Display each object's namespace using __dict__. ##
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    sparky = Dog("Sparky", 4, "Beagle", True)
    rocky = Dog("Rocky", 1, "Golden Retriever", False)

    # Print through the class
    print(f"Dog.species {Dog.species}")
    # Print through the object
    print(f"sparky.species {sparky.species}")
    print(f"rocky.species {rocky.species}")

    #Adding new attribute to only one object (sparky object)

    sparky.favorite_food = "Steak"
    print(f"Sparky's favorite food is {sparky.favorite_food}")

    # Display each object's namespace using __dict__
    print(f"instance namespace for Sparky: {sparky.__dict__}")
    print(f"instance namespace for Sparky: {rocky.__dict__}")

    # Display information about the class namespace
    print(f"Dog class:", Dog.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Dog("Max", 4, "German Shepherd", True)
    original.tricks = ["sit", "stay"]

    shallow = copy(original)

    deep = deepcopy(original)

    original.tricks.append("roll over")

    print("Original:", original.tricks)
    print("Shallow:", shallow.tricks)
    print("Deep:", deep.tricks)



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")
    animal = Animal("Goat", 5)
    print(animal.get_info())

    dog = Dog("Ziggy", 11, "Australian Shepherd", True)
    print(dog.get_info())
    print(dog.bark())


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()