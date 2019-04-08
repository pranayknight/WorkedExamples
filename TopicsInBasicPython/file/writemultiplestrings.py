f=open("myfile.txt","w")
print("Enter text(Type # whenyou are done)")
s=''
while s!="#":
    s=input()
    f.write(s)

f.close()