try:
    passw=input("Enter a password, must be atleast eight characters ")
    assert len(passw)>=8,"Invalid password entered"
except AssertionError as obj:
    print(obj)
else:
    print("Your Password is",passw)