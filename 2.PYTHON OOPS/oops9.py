'''inheritance: when child class inherits the properties of parent class.
main work: ki humko har class ka alag se object create na karna pade'''

class A: #this is parent class
    def displayA(self):
        print("this is akarsh")

class B(A): #this is child class b which inherits parent class A
    def displayB(self):
        super().displayA() # calling method from parent class using 'super' keyword
        print("This is Bharat")

obj=B() #creating object of child class
#obj.displayA()
obj.displayB()