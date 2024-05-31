class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 2)
dog2 = Dog("Max", 3)

# Accessing object attributes
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")

# Calling object methods
dog1.bark()
dog2.bark()
