try:   # wrap the code whichever might cause exception in try with the indentation to handle exception
    a,b=[int(x) for x in input("Enter two numbers: ").split()]
    c=a/b
    print(c)
except ZeroDivisionError:   #since the error that can happen here is zero division error  we can have multiple exceptions to handle the different types of errors that can happen
    print("Division by zero is not allowed")   # if we don't use anything after except then if any type of error that happens is try block the except block will be executed but here only division by zero exception is handled and a suitable message relevant to that is displayed
    print("Please enter a non zero number")
print("Code after the exception")

