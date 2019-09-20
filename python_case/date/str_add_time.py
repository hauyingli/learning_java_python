# sample: "date 2019-09-06"
import datetime
import time

now = datetime.date.today()
name = "date {}"
name_time = name.format(now)
print (name_time)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#######################################
# from datetime import datetime

# sample: "date 2019-09-06 19:31:14.431818"
# now = datetime.now()
# name = "date {}"
# name_time = name.format(now)
# print (name_time)