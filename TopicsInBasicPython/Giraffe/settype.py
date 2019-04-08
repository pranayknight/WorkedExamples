s={10,20,30,"XYZ",10,20,10}   #a set is denoted in curly brackets and does not allow duplicates
print(s)         #in this print statement all the duplicates that are present in the above set is ommitted
print(type(s))

s.update([88,99])      #set also arranges the elements within it randomly so we can't do indexing,slicing or repetition
print(s)               #here we have tried to add data to set

s.remove(20)        #we can use remove function in sets
print(s)

f=frozenset(s)   #this can be used to freeze the set and the values of the frozen set can't be changed
print(f)         #in the fozen set the set can't be updated neither can be the elements removed
