#deletion of a file: first execute "create2.py" program
import os
if os.path.exists(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\c.txt"):
    os.remove(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\c.txt")
    print("file deleted successfully")
else:
    print("file does not exists")