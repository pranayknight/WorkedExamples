'''lst=[]
for i in range(1,11):     #this is uing regular programming
    lst.append(i**3)
print(lst)'''

#now we will see it in list comprehension programming

lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)
