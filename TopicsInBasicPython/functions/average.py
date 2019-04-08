def average(a,b):      #def keyword is used to define a function
    print("Average of two numbers is: ",(a+b)/2)

average(25,67)       #here we pass on the values to the function


#let's see another example where we will invoke(call) the function

def avg(c,d):      #if we define the values hereitself as c=10,d=20 they will be called default values and can even be changed in later part where we invoke the function
    return((c+d)/2)

result=avg(c=10,d=20)  #we passed parameters using keywords so its placement can be exchanged also
print(result)
