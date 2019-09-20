import datetime
import time
import calendar


print(time.localtime())

print(datetime.datetime.now())
print(datetime.date.today())

import time
t = time.strftime("%Y%m%d",time.localtime())
print("t"+t)

import time
t = time.strftime("%m%d%S",time.localtime())
print("t"+t)