#abstraction: hidding unusefull data from user
'''hiding of logic/implementation of code from user,and just showing the interface
eg: during a incoming call,interface of red & green buttton 
work is to accept & decline, but how does it work with what logic is hidden '''

#normal abstraction: it is just like module add & sub code written in different code ,imported and used 
#with obj creating and passing the arguments and get the results

'''abstract class'''
from abc import ABC,abstractmethod
class Car(ABC):
    def show(self):
        print("every  car has four wheels")

    @abstractmethod
    def speed(self):
        pass
    
class Buggati(Car):
    def speed(self):
        print("the speed of Buggati is 450km/h")

class Lamborghini(Car):
    def speed(self):
        print("the speed of Lamborghini is 350km/h")


obj=Buggati()
obj.show()
obj.speed()

obj1=Lamborghini()
obj1.show()
obj1.speed()