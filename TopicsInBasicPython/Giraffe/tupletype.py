tpl=(40,50,40,'xyz') #if we are to define a tuple or list with one element we are to provide a comma after that element
print(tpl)

tpl1=(40)         #here since no comma is provided it considers as an int(same with the case of lists)
print(type(tpl1))

tpl2=(40,)         #if we provide the comma it will consider it as a tuple(same with the case of lists)
print(type(tpl2))

print(tpl[3])   #indexing in tuple
print(tpl*3)    #performing repetition
print(tpl.count(40))  #counting the no. of times a value appears
print(tpl.index("xyz"))


lst=[67,34,"xyz"]
print(lst)
tpl3=tuple(lst)
print(tpl3)
