# * coding:utf 8 *
# print出日期+文字
# 沒加入str
# import datetime
# date_object = datetime.date.today()
# # or date_object = datetime.now()
# print(date_object)
import datetime

# def date():
#
#     now = datetime.date.today ()
#     name = "date {}"
#     name_time = name.format (now)
#     print (name_time)
#
# date()

# f = open("Label"+name_time,'a')
# # 读取label.txt文件，没有则创建，‘a’表示再次写入时不覆盖之前的内容
# f.write("你好")
#
# f.write('\n')
# f.write("www")
# f.close()


import datetime
import os

####################################
#
# now = datetime.date.today ()
# name = "date {}"
# name_time = name.format (now)
# print (name_time)
#
# # create pic
# def screenshot():
#     # screenshot
#     os.system('adb shell screencap -p /sdcard/screentest.png')
#     # pull to latop
#     os.system("adb pull /sdcard/screentest.png /home/hauying/Desktop/auto_python/gmail")
#
#
# screenshot()

###############################
import re
f = open('/sur/test.txt')
source = f.read()
f.close()
r = r'hello'
s = len(re.findall(r,source))
print (s)