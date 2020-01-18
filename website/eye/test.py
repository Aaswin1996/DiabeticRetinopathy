import datetime
import time
a=datetime.datetime.now()
while(True):
    time.sleep(0.001)
    print("hello")

b=datetime.datetime.now()
print(b-a)