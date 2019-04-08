class Student:
    major="CSE"    #this is a static field

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s1=Student(1,"John")
s2=Student(2,"Bill")
print(s1.major,s1.name,s1.rollno)
print(s2.major,s2.name,s2.rollno)
print(Student.major)      #we can also use a static field like this
