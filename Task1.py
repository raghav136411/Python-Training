# Build a list containing the 5 filenames of the text files that are going to be used.
#(Hint: Can be done by hand or using the os.listdir('dirpath') function in the os module)
import os, sys
import functools
from random import *
path = "D:/Users/raghtiwa/Desktop/Files"
dirs = os.listdir(path)
os.chdir(path)
My_list = []
for file in dirs:
   print (file)
   My_list.append(file)
#My_list.append("bogus.txt")
print(My_list)
mm = []
for file in My_list:
    try:
        fh = open(file, "r+")
        fh.write("This " + file + " is my test file for exception handling!!")

    except IOError:
        print("Error: can\'t find file or read data"+ ". Check if file "+ file + " exist")
    else:
        print("Written content in the file successfully")
        fh.close()

for file in My_list:
    fh = open(file, "r+")
    x = str(fh.read())
    x = x.split()
    x[1] = uniform(2.5, 10.0)
    mm.append(x[1])

print(mm)
print("Average is :", float(sum(mm))/len(mm))