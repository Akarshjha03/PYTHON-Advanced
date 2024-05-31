#access modifier: private
'''variable and  method cannot be accessed within ot outside the class'''

#same as code oops16:
class Students:
    __name="AKARSH"
        
    def __info(self):
        print("welcome to bharat")

obj=Students()
#it will throw an error (cause we cant access private anywhere)
obj.__name
obj.__info()

#still want to aaccess: solution oops16 with constructor and self
class Students:
    __name="AKARSH"
    def __init__(self):
        print(self.__name)

        self.__info()

    def __info(self):
        print("welcome to bharat")

obj=Students()
