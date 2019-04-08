def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u   #it will b assigned as a tuple

result=calc(10,5)
print(result)

for i in result:print(i)
