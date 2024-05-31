try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code to handle a specific exception (if it occurs)
    print("Cannot divide by zero!")
else:
    # Code to execute if no exception is raised
    print("Division successful, result:", result)

