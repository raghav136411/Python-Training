#9.	Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".

def translate(d):
    l=0
    b=str()
    for i in d:
        if d[l] in "aeiou":
            b = b + d[l]
        else:
            b = b + d[l]+ "o" + d[l]
        l=l+1
    print(b)

a = input("Enter the String : ")
translate(a)
