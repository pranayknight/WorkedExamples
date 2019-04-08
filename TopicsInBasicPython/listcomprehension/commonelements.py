a=[2,4,6,8]
b=[1,2,3,4]
result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)

#now let's perform the same with list comprehension

desult=[j for j in a if j in b]
print(desult)

