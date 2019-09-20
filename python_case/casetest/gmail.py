# Python3.6.4
# * coding:utf 8 *
from uiautomator import device as d
from time import sleep
import os

'''opne adb command'''
# from PIL import Image  # pip install pillow


def screen():
    # d.screen.on()
    # d(resourceId="com.android.systemui:id/scrim_behind").swipe.up()
    # sleep(1)
    d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.up()
    sleep(1)


screen()


def open():
    d(text="Gmail").click()
    sleep(1)
    #d(text="GOT IT").click()
    #sleep(3)
    #d(text="TAKE ME TO GMAIL").click()
    #d(text="Next").click()
    #d(text="OK").click()
    d(resourceId="com.google.android.gm:id/compose_button").click()
    sleep(1)
    # d(text="Got it").click
    # get text info
    # d(className="android.widget.MultiAutoCompleteTextView").text
    # edit text
    d(className="android.widget.MultiAutoCompleteTextView").set_text("t20190410@gmail.com")
    d.click(463.0, 878.0)
    d.press(0x07)
    d.press(0x07)
    sleep(1)
    d(text="Subject").set_text("autotest1")
    sleep(1)
    d.click(463.0, 878.0)
    d.click(890.0,  140.0)
    sleep(2)
open()


# create pic
def screenshot():
    # screenshot
    os.system('adb shell screencap -p /sdcard/screentest.png')
    # pull to latop
    os.system('adb pull /sdcard/screentest.png /home/hauying/Desktop/auto_python/gmail ')


screenshot()





