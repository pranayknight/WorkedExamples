import os,sys

if os.path.isfile("myfile123.txt"):
    f=open("myfile123.txt","r")
    s=f.read()
    print(s)
    f.close()
else:
    print("File does not exist")
    sys.exit()
