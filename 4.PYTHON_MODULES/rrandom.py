#random in build module
import random
n = random.randint(2,8)
print("n") #this prints random number between 2&8

n1 = random.randrange(2,4)
print("Random number between 2 and 3: ", n1)

l=[10,20,30,40]
lc=random.choice(l)
print("A Random element from the list is :",[lc])

r=random.random()
print(r) #this prints float value between 0&1

p=[1,2,3,4]
random.shuffle(1)
print("Shuffled List: ", p)

u= random.uniform(3,9)
print(u)# this gives a random float between 3 & 9