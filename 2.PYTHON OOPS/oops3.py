#if we want to create a variabke inside a method then we have to use the self keyword.
class Define:
    a=10
    def sqr(self):
        self.c=self.a*self.a
        return self.c
    
obj=Define()
obj=print("Value of c is",obj.sqr())