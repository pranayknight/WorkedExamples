# Ways of adding elements to list

a = [5,12,72,55,89]
a = a+[1]
a = a+["BCD"]
a = a+list("BCD")
# a = a+list(123)  not possible because not iterable
a = a+[1,2,3]
a = a+list(str(123))
a = [5,12,72,55,89,1]
a = a+[5,6,7,8]
a = a+[[5,6,7,8]]
a.append([10,11,12,13])
# we need to keep in mind that appending a data to list returns a None value
# to see this see the following example
a = [5,12,72,55,89,1]
b = a.append(10)
print(b)
a.insert(2,100)
a.insert(2,[10,20,30])
# this insert method also returns a None type so if we assign to another value
# it will give a None (Lists are mutable)
# as they are mutable we can insert values in the given index:
a[3] = 5
print(a)
# even .remove() function will also return None type
