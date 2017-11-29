# 3.	Write a Python based program which acts as a calculator .(Menu based)


def Calculator(a):
    b = a.split()
    if b[1] == "+":
        Output = int(b[0]) + int(b[2])
    elif b[1] == "*":
        Output = int(b[0]) * int(b[2])
    elif b[1] == "-":
        Output = int(b[0]) - int(b[2])
    else:
        Output = int(b[0]) / int(b[2])
    return Output

a = input("Calculate with space b/w operator and operand : ")
Output = Calculator(a)

print("Output is : ", Output)
