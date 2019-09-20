# Python3.6.4


import os
from uiautomator import device as d
'''opne adb command'''
from PIL import Image #pip install pillow

#create pic
def screen():
    # screenshot
    os.system('adb shell screencap -p /sdcard/screentest.png') #//+time end pull all
    # # pull to latop
    os.system('adb pull /sdcard/Unknown /home/hauying/Desktop/auto_python/png ')
    d.screenshot("xxx.png")
screen()

#setup pic
# def getDistance():
#
#     #input pic
#     image = Image.open('screentest.png')
#     #output info
#     height = image.size[0]
#     width = image.size[1]
#     print(height, width)
#
#     for i in range(x, y):
#         for j in range(x, y):
#             pass
#
# getDistance()