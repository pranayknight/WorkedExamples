'''class student:
    def __init__(self):
        self.id=123                #these fields are not private yet they are public so we can acces them creating an
        self.name="John"           #object of the class to make them private we add two underscores

s=student()
print(s.id)
print(s.name)'''

'''class student:
    def __init__(self):
        self.__id=123                #these fields are now made private
        self.__name="John"

s=student()
print(s.id)                         #now we cannot access them as they are private and running this will display error
print(s.name)'''

class student:
    def __init__(self):
        self.__id=123
        self.__name="John"
                                   #we can actually access them creating another class
    def display(self):
        print(self.__id)
        print(self.__name)

s=student()
s.display()
print(s._student__id)           #so in python its not completely hidden and can be accessed like this and it is called
print(s._student__name)                                                                          #name mangling