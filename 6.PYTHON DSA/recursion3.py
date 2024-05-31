#recursion 3rd  program
#print sum from 1 to n:

'''n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''

def sum(n):
    if n==1:
        return 1
    
    answer = n + sum(n-1)
    return answer

r=sum(3)
print(r)