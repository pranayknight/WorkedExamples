our_tuple1 = 1,2,3,"A","B","C"
print(type(our_tuple1))
our_tuple = (1,2,3,"A","B","C")
print(our_tuple[0:3])
# Tuples are not mutable after they are defined same as strings
# ex:- our_tuple[2] = 100   will throw an error
# converting other pieces of data into tuple
A = [1,2,3]
B = tuple(A)
# we can define multiple variable in one shot
(A,B,C) = 1,2,3
[d,e,f] = 4,5,6             #kewl
g,h,i = 7,8,9
