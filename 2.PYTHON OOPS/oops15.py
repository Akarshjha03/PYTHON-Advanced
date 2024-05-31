#method overridding: which means same parameters and same arguments
'''we will use inheritance concept in this: the class parent and child will have method of same name
(parameters)and same arguments ,then the child class will override the method of parent class
But, with the help of super keyword the method of parent class can be called in child class'''

class A:
    def displayA(self):
        print("this is parent class")

class B(A):
    def displayA(self):
        #super().displayA()
        print("this a child  class")

obj=B()
obj.displayA()