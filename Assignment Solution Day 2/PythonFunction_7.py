#7.	Define a function that computes the length of a given list or string. (It is true that Python has the len() function
#  built in, but writing it yourself is nevertheless a good exercise.)

def length(a):
    b = list(a)
    i=0
    for l in b:
        i=i+1
    return i


a = input("Input the String: ")
size = length(a)

print("Size of String is : ", size)

