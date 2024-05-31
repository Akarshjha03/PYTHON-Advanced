#multiple inheritance:
class A: #parent class
    def displayA(self):
        print("this is akarsh")

class B: #other parent class
    def displayB(self):
        print("this is python")

class C(A,B): #child class inheriting the properties of parent class A,B both
    def displayC(self):
        print("this is bharat")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()