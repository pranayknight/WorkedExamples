class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def stop(self):
        print("Stopping the car")


    def start(self):
        print("Starting the car")

class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)   #instead of invoking BMW.__init__ way we used a built in fn super() in which we need not use the self parameter as it comes inbuilt with super()
        self.cruiseControlEnabled = cruiseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    def start(self):
        super().start()  # here we used the parent class functionality as well using super() method(invoked parent class method from child class)
        print("Button Start")      # *it is also called adding functionality on top of the existing functionality

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()
        print("Remote Start")

threeSeries=ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled, threeSeries.make, threeSeries.model, threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True, "BMW", "8i", 2019)
print(fiveSeries.parkingAssistEnabled, fiveSeries.make, fiveSeries.model, fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()