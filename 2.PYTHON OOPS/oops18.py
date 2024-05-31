#access modifiers:public
class Public:
    def __init__(self):
        self.name="AKARSH"
    def display(self):
        print(self.name) #accessing public variable inside the class
        print("this is method of public") 

'''accesing this method and varoable in different class can be done using inheritance and super'''

obj=Public()

print("accessing public variable outside class",obj.name)

print("accessing public method outside class\n",obj.display())

#and 

#accesing public method inside another method using self. keyword
class MyClass:
    def method_one(self):
        print("Executing method_one")

    def method_two(self):
        print("Executing method_two")
        
        # Call method_one from within method_two
        self.method_one()

obj1=MyClass()
obj1.method_two()
