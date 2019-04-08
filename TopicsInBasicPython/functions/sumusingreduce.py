from functools import reduce  #since reduce function has to be imported to be used

lst=[5,10,15,20]
result=reduce(lambda x,y:x+y, lst)  #to get the sum from the list
print((result))
