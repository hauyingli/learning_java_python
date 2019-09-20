from datetime import datetime
#used .now need ("from datetime import datetime")
#If used today(sample:
# import datetime
#
# now = datetime.date.today()
# name = "date {}"
# name_time = name.format(now)
# print (name_time)

now = datetime.now()
name = "date {}"
name_time = name.format (now)
print (name_time)

f = open("test"+name_time,'a')
f.write("你好")

f.write('\n')
f.write("www")
f.close()