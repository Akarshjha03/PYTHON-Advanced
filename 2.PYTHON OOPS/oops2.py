#we can use the arguments inside method:
class Machine:
    def sum(self,a,b):
        add=a+b
        return add
    
obj=Machine()
ans=obj.sum(23,45)
print(ans)