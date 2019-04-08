from threading import *

class BookMyBus:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l=Lock()  #we can also use Semaphore() in place of Lock() to perform the same work

    def buy(self,seatsRequested):
        self.l.acquire()
        print("Total seats available:",self.availableseats)

        if(self.availableseats>=seatsRequested):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printng the ticket")
            self.availableseats-=seatsRequested
        else:
            print("Sorry, no seats available")
        self.l.release()

obj=BookMyBus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()
