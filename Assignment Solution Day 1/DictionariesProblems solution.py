#Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:

#1.create a 3 key: value pair dictionary and assign it to a variable
a = {'Name': 'Raghav', 'Age': 23, 'Batch': 'Trainee'}

#2.access and print a value from the list in step 1 by key
print(a['Name'])

#3.add a fourth key: value pair to the dictionary from step 1
a['city'] = "Kanpur"

# 4.print the dictionary from step 3
print(a)

#5.print the length of the dictionary from step 3
print(len(a))


#Reassignment by Key and Del:

#1.create a 2 key: value pair dictionary and assign it to a variable
b = {'Name': 'Raghav', 'Age': 23}

# 2.print the dictionary from step 1
print(b)

# 3.reassign a key from the dictionary in step 1 a different value than its original value
b['Name'] = 'Raghu'

# 4.print the dictionary from step 3
print(b)

# remove a key: value pair from the dictionary from step 3 using del
del b['Age']

#6.print the new dictionary
print(b)