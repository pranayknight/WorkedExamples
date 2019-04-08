class course:

    def __init__(self,name,ratings):  #parameterised constructor
        self.name=name
        self.ratings=ratings


c1=course("Java course",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)

c2=course("Java Web Services",[5,5,5,5])
print(c2.name)
print(c2.ratings)
