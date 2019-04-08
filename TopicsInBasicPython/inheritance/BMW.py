#in this ptogram we saw how to inherit the fields of the parent class

class BMW:                                #this is the parent class we have made
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year


class threeseries(BMW):    #to inherit the parent class we only use it's name in bracket
    def __init__(self,cruiseControlEnabled,make,model,year): #here also we initialise the field as in parent class so the child class can use them
        BMW.__init__(self,make,model,year)  #in this first line of child class contructor we need to invoke the parent class constructor
        self.cruisecontrolenabled=cruiseControlEnabled


class fiveseries(BMW):
    def __init__(self,parkingassistenabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingassistenabled=parkingassistenabled

threeseries=threeseries(True,"BMW","328i",2018)  #thus we created object of the child class invoking that class and defining variables
print(threeseries.cruisecontrolenabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)

fiveseries=fiveseries(True,"BMW","8i",2019)  #thus we created object of the child class invoking that class and defining variables
print(fiveseries.parkingassistenabled)
print(fiveseries.make)
print(fiveseries.model)
print(fiveseries.year)
