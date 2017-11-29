# 11.	Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(s):
    d = str()
    d = s[::-1]
    return d

a = input("Enter the String : ")
print("Reverse of the string is : ", reverse(a))