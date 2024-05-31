#code for a reading a file:

f=open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\a.txt","r")
print(f.read())
#f.read(30) will read only 30 characters from start
#f.readlines()  reads all lines in the file and returns as a list of strings
f.close() #is used to close the file after we are done with it
print("file has been read successfully")