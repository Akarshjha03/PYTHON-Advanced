class MinStack:
    def __init__(self, capacity):
        self.stack = []
        self.min_stack = []  # Stack to track minimum elements efficiently
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.stack.append(value)

        # Update min_stack only if the pushed value is less than or equal to the current min:
        if self.is_empty() or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            # Maintain the min_stack without redundant elements (optimization):
            while self.min_stack and self.min_stack[-1] > value:
                self.min_stack.pop()
            self.min_stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return
        popped = self.stack.pop()

        # Update min_stack only if the popped value was also the current min:
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        return popped

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def get_min(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.min_stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements (top to bottom):")
        for value in reversed(self.stack):
            print(value)


# Example usage
min_stack = MinStack(5)
min_stack.push(3)
min_stack.push(2)
min_stack.push(5)
min_stack.push(1)
min_stack.push(4)

print("Top element:", min_stack.top())
print("Minimum element:", min_stack.get_min())

min_stack.display()

print("Popped:", min_stack.pop())
print("Minimum element:", min_stack.get_min())

min_stack.display()
