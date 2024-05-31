#code to appendd a file:


f=open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\d.txt","w")
f.write("hello \n I am akarsh jha \n i am 20 years old \n i like to code \n")
f.close()

#actual appending:
f=open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\d.txt","a")
f.write("Akarsh petname is gullu")
f.close()
print("file appended successfully")