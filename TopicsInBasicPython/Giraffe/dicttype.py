dict1={1:"john",2:"bob",3:"bill"}  #a dictionary contains keys and values separated by colon within curly brackets
                                  #both keys or values can be of numeric or string data types as desired by user
print(dict1)

print(dict1.items())   #gives all the keys and values of the dictionary
print(dict1.values())  #gives all the values of the dictionary
print(dict1.keys())    #gives all the keys of the dictionary
# we can also use for loops using keys or values to display the keys or values line by line

k=dict1.keys()
for i in k:print(i)

l=dict1.values()
for j in l:print(j)

print(dict1[2]) #printing values from the related keys

del dict1[2]  #this way we can delete items from dictionary using the related keys
