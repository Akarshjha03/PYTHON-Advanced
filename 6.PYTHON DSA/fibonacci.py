#fibonacci series:

# Number of terms you want to print
n = 7

# Initialize the first two terms
a, b = 0, 1

# Print the first two terms
print(a, b, end=" ")

# Compute and print the rest of the terms
for _ in range(n - 2):
    a, b = b, a + b 
    print(b, end=" ")