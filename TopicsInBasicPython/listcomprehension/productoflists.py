a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)
#now lets do that with the help of list apprehension

x=[]
x=[a[j]*b[j] for j in range(len(a))]
print(x)