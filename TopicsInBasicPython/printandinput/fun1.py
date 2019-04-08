primeflag=True
x=int(input("Enter a number"))

for i in (2,(x-1)):
    if x%i==0:
        primeflag=False

if primeflag==True:
    print("It is a prime number")
else:
    print("It is a composite no.")
