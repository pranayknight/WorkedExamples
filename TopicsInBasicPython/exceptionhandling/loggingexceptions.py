import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)   #now we can log anywhere
try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter two numbers: ").split()]
    c=a/b
    logging.info("Division in progress")
    f.write("Writing %d to file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("division by zero")

else:
    print("You have entered a non zero number")

finally:
    f.close()
    print("File closed")

print("Code after the exception")
