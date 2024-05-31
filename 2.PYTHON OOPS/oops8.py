'''Create a Rectangle class:
Attributes: length, width
Methods: area(), perimeter()'''

class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        current_area=self.length*self.width
        return current_area
    
    def perimeter(self):
        current_perimeter=2*(self.length + self.width)
        return current_perimeter
    
val1=Rectangle(3,4)
print("Area of the rectangle is", val1.area())
print("Perimeter of the rectangle is", val1.perimeter())
val2=Rectangle(5,6)
print("Area of the rectangle is", val2.area())
print("Perimeter of the rectangle is", val2.perimeter())
