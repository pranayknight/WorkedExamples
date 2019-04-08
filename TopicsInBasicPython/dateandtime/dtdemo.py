import time,datetime

epochseconds=time.time()
print(epochseconds)
t=time.ctime(epochseconds)
print(t)

dt=datetime.datetime.today()
print(dt)
print(dt.day,dt.month,dt.year)
print(dt.hour,dt.minute,dt.second)

print("Current Date- {}/{}/{}".format(dt.day,dt.month,dt.year))  #curly brackets are the place holders here
print("Current Time- {}:{}:{}".format(dt.hour,dt.minute,dt.second))
