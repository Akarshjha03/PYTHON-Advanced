#first practical oops code:

#creating of class:
class Person: #class name 1st letter should be capital eg: Person , Car_machine or CarMachine
    a=23
    def add(self): #method ie.function inside a class
        sum=27+3
        return sum
    
#creating a object assigning a class and using its methods: 
obj=Person() #object is nothing but just like variable here which is assigned a class for its method and variable use
print(obj.a)
print(obj.add())
#we can create as many objects as we want
obj1=Person()
print(obj1.a)
print(obj1.add)
