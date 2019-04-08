try:
    num=int(input("Enter an even no."))
    assert num%2==0,"You have entered an invalid input or odd no."
except AssertionError as obj:
    print(obj)
print("After the assertion")
