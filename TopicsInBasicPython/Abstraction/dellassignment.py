from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    def __init__(self,year):
        self.year=year

    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def __init__(self,make,year):
        super().__init__(year)
        self.make=make

    def scroll(self):
        print("Scrolling(HP)")

class DELL(TouchScreenLaptop):
    def __init__(self,make,year):
        super().__init__(year)
        self.make=make

    def scroll(self):
        print("Scrolling(Dell)")

class HpNotebook(HP):
    def __init__(self,make,year):
        super().__init__(make,year)

    def click(self):
        print("Click(HP)")

class DellNotebook(DELL):
    def __init__(self,make,year):
        super().__init__(make,year)

    def click(self):
        print("Click(DELL)")

dn=DellNotebook("Dell","2018")
hp=HpNotebook("HP","2019")
print(dn.make)
print(dn.year)
print(hp.make)
print(hp.year)
