#getter & setter method:
'''whenever we want to set a value in variable/method of private,we use this
setter: means setting the value
getter: means getting the value'''

class Students:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=Students()
obj.setname("AKARSH")
name=obj.getname()
print(name)