'''A program that reads a text file and counts the number of words in it.'''

# Open the file
file = open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\b.txt", "r")  # replace with your file name

# Read the file
text = file.read()
print(text)

# Split the text into words
words = text.split()
text = file.read()
print(text)
# Count the number of words
num_words = len(words)

# Print the number of words
print(f"The file has {num_words} words.")

# Close the file
file.close()
