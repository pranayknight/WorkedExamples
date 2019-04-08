from abc import ABC, abstractmethod


class TouchScreenLaptop(ABC):
    def __init__(self,year):
        self.year = year

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def __init__(self,year):
        TouchScreenLaptop.__init__(self,year)
        pass

    def scroll(self):
        print("Scrolling in action in HP Laptop")

class Dell(TouchScreenLaptop):
    def __init__(self,year):
        TouchScreenLaptop.__init__(self,year)
        pass

    def scroll(self):
        print("Scrolling in action in Dell Laptop")

class HPNotebook(HP):
    def __init__(self,year):
        HP.__init__(self,year)
        print("Hp Notebook is starting")

    def click(self):
        print("Click in action in HP notebook")

class DellNotebook(Dell):
    def __init__(self,year):
        Dell.__init__(self,year)
        print("Dell Notebook is starting")

    def click(self):
        print("Click in action in Dell notebook")

h = HPNotebook(2003)
h.scroll()
h.click()

d = DellNotebook(2019)
d.click()
d.scroll()