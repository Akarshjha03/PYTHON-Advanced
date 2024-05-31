#code to copy a file:

with open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\a.txt","r") as f:
    with open(r"C:\Users\akars\OneDrive\Desktop\CODING\PYTHON FILEHANDELING\b.txt","w") as f2:
        for i in f:
            f2.write(i)
f.close()
f2.close()

print("the data has been successfully copied")


#same code inside exception is other file is not found or created
'''try:
    with open("C:\\Users\\DELL\\Desktop\\python\B.txt") as f:
        with open("C:\\Users\\DELL\\Desktop\\python\B.txt", "w") as f2:
            for i in f:
                f2.write(i)

except FileNotFoundError:
    print("file not available ... plz create first!")

else:
    f.close()
    print("file closed successfully")
'''