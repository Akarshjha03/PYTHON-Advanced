#hybrid inheritance: mix of multilevel and hierrarical inheritance
class A: #parent class 
    def displayA(self):
        print("this is akarsh")

class B: #other parent class 
    def displayB(self):
        print("this is jha")

class C(A,B): #child class inheriting parent class A,B (parent class for class D)
    def displayC(self):
        print("this is bharat")
#object of class C
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

class D(C): #child  class inheriting class C
    def displayD(self):
        print("hello")
#object of class D
obj1=D()
obj1.displayA()
obj1.displayB()
obj1.displayC()
obj1.displayD()