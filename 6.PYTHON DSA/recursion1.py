#1st recursion program:
#factorial of n-1

def factorial(n):
    #base case:
    if n==0:
        return 1
    #recursive case:
    else:
        ans = n*factorial(n-1)
        return ans

#result=factorial(5)
#print(result)

#OR

n=int(input("Enter the number:"))
result=factorial(n)
print(result)