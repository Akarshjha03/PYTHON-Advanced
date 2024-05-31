#recursion 4th  
#recursion for power
'''a=2
b=3
c=a**b
print(c)'''

def power_a_b(a,b):
    if b==0:
        return 1
    
    answer= a*power_a_b(a,b-1)
    return answer

a=int(input("Enter the base number : "))
b=int(input("Enter the exponent : "))
print(power_a_b(a,b))
