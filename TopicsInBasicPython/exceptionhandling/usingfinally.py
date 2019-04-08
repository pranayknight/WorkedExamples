try:
    f=open("myfile","w")  # the syntex used to open file named myfile and permission as write
    a,b=[int(x) for x in input("Enter two numbers: ").split()]
    c=a/b
    f.write("Writing %d to file"%c)  # if we close file right after this if error happens it will not be closed
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")

else:       # if there is no error the except will not be executed and the program comes to else and it gets executed
    print("You have entered a non zero number")

finally:                          # this is the best place to use finally block and will be executed no matter what
    f.close()
    print("File closed")

print("Code after the exception")