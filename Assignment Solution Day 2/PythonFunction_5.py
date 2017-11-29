# 5.	Define a function max() that takes two numbers as arguments and returns the largest of them.
#  Use the if-then-else construct available in Python.
# (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

def max(a, b):
    if a>b:
        print("Bigger No is : ", a)
    else:
        print("Bigger No is : ", b)

a = input("Enter first number : ")
b = input("Enter second number : ")
max(a, b)

