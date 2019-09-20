from datetime import datetime
import re

now = datetime.now()
name = "date {}"
name_time = name.format(now)
print (name_time)

f = open(name_time,'a')
f.write(name_time)

f.write('\n')

f.close()
