students = {}
students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
print(students)
print(students["Dan"])
students["Fred"]=25
print(students["Alice"])
students["Alice"]=26
print(students["Alice"])

del students["Fred"]
print(students)

print(students.keys())
# Note that Dictionary type doesn't support indexing of keys
# But to have it in our indexing manner we need to assign it to a list

a = list(students.keys())
print(a[0],a[3])

# Same with the values of the dictionary and we can perform slicing indexing etc

b = list(students.values())
print(b[0],b[3])
# same as above but without assigning so as to save space and time
print(list(students.values())[2])
