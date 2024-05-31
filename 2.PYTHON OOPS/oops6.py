'''Create a Person class:
Attributes: name, age, gender
Methods: say_hello (prints a greeting message with the person’s name)'''

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def say_hello(self):
        print(f"persons name is {self.name},age is {self.age},gender is {self.gender}")

per1=Person("AKARSH",20,"Male")
per1.say_hello()
per2=Person("Nitish",22,"Male")
per2.say_hello()
per3=Person("Ritika",20,"Female")
per3.say_hello()