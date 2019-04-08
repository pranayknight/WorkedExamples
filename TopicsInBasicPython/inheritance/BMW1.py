# Here we will also inherit the functionality from parent class


class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def stop(self):
        print("Stopping the car")


    def start(self):                        # defining methods in parent class to use in child class
        print("Starting the car")

class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    def display(self):               #this display method is only available in this child class not in parent class nor in FiveSeries
        print(self.cruiseControlEnabled)
    def start(self):                        #we are overriding or shadowing the method in sub class to have diff functinality
        print("Button Start")

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

threeSeries=ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled, threeSeries.make, threeSeries.model, threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True, "BMW", "8i", 2019)
print(fiveSeries.parkingAssistEnabled, fiveSeries.make, fiveSeries.model, fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()