'''Write a Python class named Rectangle to represent a rectangle shape.
The class should have the following functionalities:
1.A method named set_dimensions that takes two parameters width and
height and sets the attributes of the rectangle object accordingly.
2.A method named area that calculates and returns the area of the
rectangle
3.A method named perimeter that calculates and returns the perimeter of
the rectangle
Use this to create objects of the class and print the width, height, area and
perimeter'''

#creating a class,methods,attribute:
class Rectangle:
    def set_dimensions(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
        
# Creating an instance of Rectangle(objects):
value1=Rectangle()
value1.set_dimensions(23,100)

# Accessing attributes and printing values:
print("value of width is:", value1.width)
print("value of height is:", value1.height)
print("Area is:",value1.area())
print("Perimeter is:",value1.perimeter())