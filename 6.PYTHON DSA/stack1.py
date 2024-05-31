#implementing and using stack

class Stack:
    def __init__(self,max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        if len(self.items) == self.max_size:
            print("Stack overflow")
        else:
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return  self.items[-1] 
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:")
            for item in self.items[::-1]:  # Print items in top-to-bottom order
                print(item)

# Creating a stack object with a maximum size of 3
stack = Stack(3)

# Pushing items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

#Displaying the stack
stack.display()  # Output: Stack elements: 30 20 10

# Pushing another item (should cause stack overflow)
stack.push(40)

# Popping items from the stack
popped = stack.pop()
print("Top item:", popped) # Output: Popped item: 30

print("Top item:" ,stack.peek()) # Output: Top item: 20

# Checking if the stack is empty
print("Is stack empty?", stack.is_empty()) # Output: Is stack empty? False