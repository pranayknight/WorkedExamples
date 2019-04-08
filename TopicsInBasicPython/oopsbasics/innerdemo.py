class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("engine Started")

c=car("BMW",2017)
e=c.engine(678)
e.start()
