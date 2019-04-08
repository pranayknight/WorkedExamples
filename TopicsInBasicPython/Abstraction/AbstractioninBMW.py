from abc import abstractmethod,ABC      #we have to import abstractmethod decorator from abc in order to use it
class BMW(ABC):    #in order to make abstraction work the parent class should inherit from a class called ABC
    def __init__(self,make,model,year):    #after making it abstract program is mandating the implementation of drive method
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    @abstractmethod           #this defines that the function is abstract
    def drive(self):   #creating an abstract method in parent class
        pass

class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button Start")

    def drive(self):
        print("Three Series is being driven")  # we can never instantiate abstract method , it will show error message

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled

    def start(self):
        super().start()
        print("Remote Start")

    def drive(self):
        print("Five Series is being driven")


threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
