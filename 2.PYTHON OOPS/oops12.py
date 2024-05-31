#hierrarical inheritance: (one parent ,many child)
class A: #parent class (class A object cssn also be made but it will only be able to access mehtods of class A)
    def displayA(self):
        print("this is akarsh")

class B(A): #child class B inheriting parent class A
    def displayB(self):
        print("this is jha")

#object of class B
obj=B()
obj.displayA()
obj.displayB()

class C(A): #child class C inheriting parent class A
    def displayC(self):
        print("this is bharat")

#object of class A
obj1=C()
obj1.displayA()
obj1.displayC()