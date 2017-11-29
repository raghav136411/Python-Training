# 6.	Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max(a, b):
    if a>b:
        return a
    else:
        return b

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")
d = max(a, b)
e = max(c, d)
print("Max of three is : ", e)
