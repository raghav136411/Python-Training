#Tuples

#1.create a 4 element tuple that consists of a float, an integer, a Boolean value, and a string.  Assingn this tuple to a  variable
a = ('hello', True, 1, 1.5)

#2.print the tuple from step
print(a)

# 3.print the the second element from the tuple you made in step 1
print(a[1])

# 4.print the first element from the tuple you made in step 1
print(a[0])

# 5.slice and print the first 3 elements of the tuple from step 1
print(a[:3])

# slice and print the last 3 elements of the tuple from step 1
print(a[-3:])

# 7.slice and print the middle 2 elements of the tuple from step 1
print(a[1:-1])


#For Loop

# 1.create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
b = ("Bohr", "Leibniz", "Einstein")

#2.create a variable and assign it an empty list
c = []

# create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
d = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4.use a for loop to go through and print each of the elements from the tuple in step 1 individually
for i in a:
    print (i)

# use a for loop and .append() to add the middle 6 elements to the empty list from step 2
for i in range(2, 8):
    c.append(d[i])

#print the new list
print(c)
