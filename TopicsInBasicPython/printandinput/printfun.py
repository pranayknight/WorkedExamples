print()
print("Hello"*3)
print("All the power is within you")
print("All that you can \n see is not true")

a,b=20,30
print(a,b)                #this prints a and b in the same line separated by a space
print(a,b,sep=",")       #we can use specific separators to print between the variables
print(a,b,sep="++++")

name="John Johny Janardan"
marks=94.5678

print("The name is",name,"and the marks are",marks)
print("Name is %s, and marks is %f"%(name,marks))   #%s is for string data similarly %i->integer, %f->float
print("Name is %s, and marks is %.2f"%(name,marks))  #we can restrict the decimal values to be displayed
print("Name is %s, and marks is %.3f"%(name,marks))


print("Namme is {}, marks are {}".format(name,marks))  #here we cannot restrict the no. of decimals
print("Namme is {0}, marks are {1}".format(name,marks)) #we can also pass the index here
