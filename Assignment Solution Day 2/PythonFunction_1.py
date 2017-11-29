# 1.	Write a function to print the fibanocci series

n = int(input("No of terms in fabonacci series =  "))
def fab(n):
    a = 0
    b = 1
    print("Fabonacci Series is : ")
    print(a)
    print(b)
    for i in range(2, n):
        s = a + b
        print(s)
        a = b
        b = s
fab(n)



