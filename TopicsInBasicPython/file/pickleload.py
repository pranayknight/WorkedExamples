import pickle

f=open("Student.dat","rb")
obj=pickle.load(f)
obj.display()
