a=13
b=100                   #here we are defining data types of type integer
c=-66
print(a,b,c)
print(type(a))         #this function is used to get what data type the particular variable is

x=33.5
y=-25.8                #here we are defining data of float type
z=205.0
print(x,y,z)
print(type(z))

d=3+5j                 #we defined d as a complex data type writing in complex form
print(d)
print(type(d))

e=0b1010               #here we defined data type of binary type in which binary code is written after 0b
print(e)

f=0xff                 #hexadecimal type writing 0x before the hexadecimal code
print(f)

g=0o56                 #octadecimal type 0o
print(g)

g=True                 #boolean type
print(g)
print(type(g))
print(9>8)
print(9<8)

h=int(x)               #converting float type to int
print(h)
print(type(h))

i=float("22.5")        #converting a string to float
print(i)
print(type(i))

j=bin(10)              #converting decimal no. to a binary no.
print(j)
print(type(j))

print(hex(10))         #converting decimal to hexa....and so on oct() for octadecimal
