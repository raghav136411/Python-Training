# 10.	Define a function sum() and a function multiply() that sums and multiplies (respectively)
# all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10
# , and multiply([1, 2, 3, 4]) should return 24.

def sum(c):
    l=0
    s=0
    for i in c:
        s = s + int(c[l])
        l=l+1
    print("Sum : ", s)

def multiply(c):
    l=0
    m=1
    for i in c:
        m = m * int(c[l])
        l=l+1
    print("Multiplication : ", m)

a = input("Input the numbers : ")
b = a.split()
choice = int(input("1 for Sum \n2 for Multiply\nGive Choice : "))
if choice == 1:
    sum(b)
else:
    multiply(b)