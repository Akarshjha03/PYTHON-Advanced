#recursion 2nd question of printing a number from 1-10

#n=int(input("Enter the range:"))
#for i in range(1,n+1):
    #print(i)

'''def printnum(n):
    #base case
    if n==0:
        return
    
    #recursive case
    else:
        for i in range(1,n+1):
            print(i)
            

n=int(input("Enter the value of n :"))
answer=printnum(n)
print(answer)'''

#prefered:
def printnum(n):
    #base case
    if n==0:
        return

    #recursive case
    print(n)
    printnum(n-1)

    #OR
    #printnum(n-1)
    #print(n)
    
answer=printnum(7)
print(answer)