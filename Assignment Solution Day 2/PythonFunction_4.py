#4.	Write a program which acts as a calculator (function based)


def calculator(n ,b):
    if(n==1):
        Output = float(b[0]) + float(b[1])
    elif(n==2):
        Output = float(b[0]) - float(b[1])
    elif(n==3):
        Output = float(b[0]) * float(b[1])
    elif(n==4):
        Output = float(b[0]) / float(b[1])
    print("Output is : ", Output)

n= int(input("Choose: 1 for Add, 2 for Sub,3 for Mul, 4 for Div : "))
a = input("Input two numbers : ")
b = a.split()
calculator (n ,b)
