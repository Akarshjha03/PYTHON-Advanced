#interface in abstraction:
'''when a abstract class only has abstract method and no normal methods its known as insterface'''
#@abstractmethod is a decorator which is used ro declare a method as abstract in abstract class
'''in interface also we cant create object in abstract class because at the end it is abstract only
which has properties that a object cannot be created in abstract class'''


from abc import ABC,abstractmethod
class Geometry(ABC):
    @abstractmethod
    def shape(self):
        pass

class Circle(Geometry):
    def shape(self):
        print("a circle is circular in shape")

class Square(Geometry):
    def shape(self):
        print("A square has 4 sides")

obj=Circle()
obj.shape()
obj1=Square()
obj1.shape()
