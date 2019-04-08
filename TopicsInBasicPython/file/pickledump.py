import pickle,student   #importing pickle for the dumping and student module from where the data is taken for pickling

f=open("Student.dat","wb")
s=student.Student(456,"John Johny",90)
pickle.dump(s,f)   #takes in two parameter first the object we want to dump and second the file we want to dump to or serialize it
f.close()