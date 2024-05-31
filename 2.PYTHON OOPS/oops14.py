'''polymorphism:one name but many forms like length() which finds us the length of string and list
in which the name is same ie.length but datattypes inside changed '''

#it has 2 types method overloading and method overridding

#method overloading: means same paramerters but different arguments:

class Area:
    def measures(self,a=None,b=None):
        if a!=None and b!=None:
            print(f"Area of rectangle is {a*b}")
        
        elif a!=None:
            print(f"Area of square is{a*a}")

        else:
            print("Nothing can be calculated")

obj=Area()
#now see different arguments in same parameter: 
obj.measures(10)
obj.measures(23,10)
obj.measures()