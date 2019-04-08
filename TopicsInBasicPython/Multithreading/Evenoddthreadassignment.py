from threading import *

class EvenNumberThread:
    def __init__(self):
        self.c=Condition()

    def EvenSeries(self):
        self.c.acquire()
        for i in range(2,101,2):
            print(i)
        self.c.notify()
        self.c.release()

class OddNumberThread:
    def __init__(self,newS):
        self.newS=newS

    def Oddseries(self):
        self.newS.c.acquire()
        self.newS.c.wait(timeout=0)
        self.newS.c.release()
        for j in range(1,100,2):
            print(j)

class SimpleSeries:
    def Series(self):
        for k in range(1,101):
            print(k)

e=EvenNumberThread()
o=OddNumberThread(e)
s=SimpleSeries()
s.Series()

t1=Thread(target=e.EvenSeries)
t2=Thread(target=o.Oddseries)

t1.start()
t2.start()
