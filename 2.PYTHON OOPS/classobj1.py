'''inside a class we can have variable and methods
with an object(variable outside class) ,we can asssign a class to an object
then the object can access the variable and methods of a class 
it can be done by calling that variable and method of a class '''

class Demo:
    a=23

    def addition(self):
        sum=10+5
        return sum
    
obj1=Demo() #creating an instance/object of Demo class
print("Value of a in obj1 is :",obj1.a)#accessing the variable 'a' through the object 'obj1'
#calling the method 'addition' through the object 'obj1'
print(obj1.addition())


obj2=Demo()
print("\nValue of a in obj2 is : ",obj2.a)
print(obj2.addition())


'''functions outside the class are known as functions only
But,functions inside the class is knows as methods'''

'''constructors are special methods that need not to be called
jaab bhi hum kisi bhi class ka object banate hai tho constructor apne aap hi call ho jata hai'''

#agar methods ke aandar variable ka use karna hai tho har samay usse self ke saath define karna hoga
'''
class Variation:
    a=10
    def square(self):
        self.c=self.a*self.a  #instead of c = a*a
        print(self.c)
        
obj1=Variation()
print(obj1.square())'''