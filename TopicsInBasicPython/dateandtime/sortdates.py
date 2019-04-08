from datetime import *
import time
startTime=time.perf_counter()
dt=[]
d1=date(2012,1,30)
d2=date(2012,1,13)
d3=date(2013,2,14)
dt.append(d1)
dt.append(d2)
dt.append(d3)

dt.sort()

time.sleep(3)    #this makes the program to wait for the specified seconds and is contained in the time module
for i in dt:print(i)
endTime=time.perf_counter()
print("Execution time: ",endTime-startTime)
