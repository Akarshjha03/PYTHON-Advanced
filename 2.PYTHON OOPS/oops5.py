#creating a actuall code using class, methods, objects ,constructors,self
class Students:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

stu1=Students("akarsh",20,"Mumbai")
stu2=Students("Mehendi",35,"Delhi")
stu3=Students("Rahul",40,"Bangalore")
stu4=Students("suthar",67,"Hyderabad")

#accessing the attributes of an object
print(f"Name:{stu1.name},Age:{stu1.age} City:{stu1.city}")
print(f"Name:{stu2.name},Age:{stu2.age} City:{stu2.city}")
print(f"Name:{stu3.name},Age:{stu3.age} City:{stu3.city}")
print(f"Name:{stu4.name},Age:{stu4.age} City:{stu4.city}")
