lst=[20,30,40,234]  #here we are defining a list    *note that in a byte max we can store is 255
print(type(lst))
b=bytes(lst)    # we used this method to change the list in the form of byte
print(type(b))
#b[3]=22   if we use this it will display an error message that bytes data types doesn't support item assignment

b1=bytearray(lst)     #by this we can define a byte array
print(type(b1))
b1[2]=33        #we can add elements in byte array  although we cannot use slicing or indexing in bytes or bytearray

print(b[2])    #we can do indexing in both bytes and bytearray
print(b1[3])