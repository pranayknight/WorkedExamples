print("Hello".count('e'))
print("happy birthday".count('day'))

happy = "happy birthday"
print(happy.upper())
print(happy.title())
print(happy.capitalize())

x = happy.title()
print(x.lower())
print(x.islower())
print(x.isupper())
print(x.istitle())
print(x.isalpha())

a = "786"
print(a.isdigit())

y = "73987ghjg"
print(y.isalnum())

print(happy.index("birthday"))
print(happy.find("birthday"))
# print(happy.index("hjhjg"))   It will throw an error
print(happy.find("hjghjgfdsj"))

z = "0000birthday0000"
print(z.strip("0"))
print(z.rstrip("0"))
print(z.lstrip("0"))
z = "   birthday    "
print(z.strip())
print(len(z))

print(x.join(y))
