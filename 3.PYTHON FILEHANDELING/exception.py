#code for exception in file handeling:

try:
    f=open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\b.txt","r")
    print(f.read())
except:
    print("file not found,  please create the file first.")
else:
    f.close()
    print("file is closed")