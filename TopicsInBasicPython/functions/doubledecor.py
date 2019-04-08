def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner

def num():
    return 5

resultfun=decor(num)    #instead of doing this we might use @decoratorname i.e @decor just above the fn we need to decorate
print(resultfun())      #here we can simply invoke the num fn after using @decor to decorate the num fn <print(num())>
