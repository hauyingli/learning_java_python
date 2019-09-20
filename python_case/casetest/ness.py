# Python3.6.4
# * coding:utf 8 *

from uiautomator import device as d
from time import sleep
import os
from PIL import Image


def screen():
    # d.screen.on()
    # d(resourceId="com.android.systemui:id/scrim_behind").swipe.up()
    # sleep(1)
    d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(resourceId="com.android.systemui:id/settings_button").click()
    d(resourceId="com.android.settings:id/settings_homepage_container").swipe.up()
    d(resourceId="com.android.settings:id/settings_homepage_container").swipe.up()
    d(text="System").click()
    d(text="Advanced").click()
    d(text="Multiple users").click()
    d(text="Add user").click()
    d(text="OK").click()
    d(text="Set up now").click()
    d(resourceId="com.android.systemui:id/scrim_behind").swipe.up()
    d(text="Continue").click()
    sleep(80)
    d(text="Skip").click()
    sleep(1)
    d(text="Skip").click()
    sleep(1)
    d(text="More").click()
    sleep(1)
    d(text="Accept").click()
    sleep(1)
    d(text="Skip").click()
    sleep(1)
    d(text="Skip").click()
    sleep(1)
    d(text="No thanks").click()
    d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.up()


screen()


def open():
    d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(resourceId="com.android.systemui:id/multi_user_switch").click()
    sleep(1)
    d(text="MORE SETTINGS").click()
    d(text="You (New user)").click()
    d(resourceId="com.android.settings:id/user_photo").click()
    sleep(1)
    d(text="Take a photo").click()
    sleep(1)
    d(text="Allow only while using the app").click()
    sleep(5)
    d(resourceId="com.google.android.GoogleCamera:id/shutter_button").click()
    sleep(1)
    d(resourceId="com.google.android.GoogleCamera:id/shutter_button").click()
    sleep(1)
    d(text="Done").click()
    d(text="New user").set_text("Big")
    d(text="OK").click()


open()


# create pic
time = 1
def screenshot():
    # screenshot
    os.system("adb shell screencap -p /sdcard/screentest'+date'.png")
    # pull to latop
    os.system("adb pull /sdcard/screentest+'date'.png /home/hauying/Desktop/auto_python/newuser ")


screenshot()



