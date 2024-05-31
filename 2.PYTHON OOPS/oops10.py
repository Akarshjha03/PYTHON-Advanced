#multilevel inheritance:
class A: #parent class
    def displayA(self):
        print("this is akarsh")

class B(A): #child class inheriting from parent class 'A'
    def displayB(self):
        print("this is jha")

class C(B): #child class inheriting from parent class 'B'
    def displayC(self):
        print("this is bharat")

#calling the methods of child classes using objects of respective classes.
#these objects are created in class c
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
