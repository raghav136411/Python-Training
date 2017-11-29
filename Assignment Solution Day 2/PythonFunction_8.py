# 8.	Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def Checking_Vowel(a):
    if a in "aeiou":
        print("True")
    else:
        print("False")
        
a = input("Enter a character : ")
Checking_Vowel(a)
