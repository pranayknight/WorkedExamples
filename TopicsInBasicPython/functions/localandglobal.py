x=123

def display():
    y=678   #since it is defined inside the function it can be used within the function only and is local
    print(x)     #since x is defined before and outside the function it is global and can be used anywhere
    print(y)
print(x)


#now lets see this example and try to analyse what's been done
def disp():
    x=897
    print(x)
    print(globals()['x'])  #this is the syntax to access global variable with same name as in function
print(x)
disp()

z=disp  #here we can also assign a function to another function
z()     #we can invoke the new function that is defined with old function and invoke the same eventually
