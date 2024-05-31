'''A program that reads a CSV file and calculates the average of the values in a 
specified column'''

# Open the CSV file
file = open(r"C:\Users\akars\Downloads\innfo.csv", 'r')

# Initialize variables
total = 0
count = 0
column_index = None

# Read the file line by line
for line in file:
    # Print the line
    print(line.strip())

    # Split the line into values
    values = line.strip().split(',')

    # Get the index of the specified column from the first line
    if column_index is None:
        column_index = values.index('Age')
        continue

    # Check if the value is numeric
    if values[column_index].replace('.', '', 1).isdigit():
        # Add the value in the specified column to the total
        total += float(values[column_index])

        # Count the number of values
        count += 1

# Calculate the average
average = total / count if count != 0 else 0

# Print the average
print('Average:', average)

# Close the file
file.close()
