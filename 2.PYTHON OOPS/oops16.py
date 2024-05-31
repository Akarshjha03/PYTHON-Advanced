#encapsulation :
'''this cconstains access modifiers: public,protected,private'''

'''for this topic we will talk about private:which cannot be accessed anywhere 
ie.inside or outside of a class'''

'''but if you want to do it you can do it  through getter and setter methods 
which will se in oops17
in this we will talk about other methods ie.with constructors'''

class Students:
    __name="AKARSH"
    def __init__(self):
        print(self.__name)

        self.__info()

    def __info(self):
        print("welcome to bharat")

obj=Students()