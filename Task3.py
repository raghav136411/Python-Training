#Write a program that tries to read a file corresponding to the first command-line argument. Provide useful feedback
# if the file doesn't exist or anything goes wrong reading the file


import sys
file=sys.argv[1]
print(file)

try:
    file_object=open(file,'r+')
    print("File successfully opened")
except FileNotFoundError:
    print("File doesn't exist")
except IOError:
    print("Couldn't read the file properly")
