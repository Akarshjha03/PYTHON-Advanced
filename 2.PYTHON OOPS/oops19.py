#access modifier: protected 
'''variables and methods can be accessed inside the class not outside'''
class A:
    def __init__(self):
        self._name="akarsh"

    def _display(self):
        print(self._name) #accesing protected variable inside class
        print("this is a protected method a")

    def _displayB(self):
        self._display() #accessing protected mathod() inside class
        print("this is mothod b")

obj=A()

#it will print (as it is allowed but not recommended)
print("accesing the protected variable outside class",obj._name)

print("accesing the protected method outside class",obj._display())