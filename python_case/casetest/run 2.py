# Python3.6.4
# * coding:utf 8 *

from uiautomator import device as d
from time import sleep
import os
from PIL import Image

try:

    def screen():
        # d.screen.on()
        # d(resourceId="com.android.systemui:id/scrim_behind").swipe.up()
        # sleep(1)
        d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.up()
        sleep(1)


    screen()


    def open():
        d(text="Phone").click()
        sleep(1)
        ##d(text="GOT IT").click()
        ##sleep(3)
        ##d(text="TAKE ME TO GMAIL").click()
        ##d(text="Next").click()
        ##d(text="OK").click()
        d(resourceId="com.google.android.dialer:id/fab").click()
        sleep(1)
        d(text="0").click()
        # sleep(0.01)
        d(text="9").click()
        # sleep(0.1)
        d(text="8").click()
        # sleep(0.01)
        d(text="8").click()
        # sleep(0.01)
        d(text="4").click()
        # sleep(0.01)
        d(text="8").click()
        # sleep(0.01)
        d(text="4").click()
        # sleep(0.01)
        d(text="6").click()
        # sleep(0.01)
        d(text="7").click()
        # sleep(0.01)
        d(text="5").click()
        # sleep(0.01)
        d(resourceId="com.google.android.dialer:id/dialpad_floating_action_button").click()
        sleep(5)
        d(resourceId="com.google.android.dialer:id/incall_end_call").click()
        sleep(2)
        d(text="Recents").click()


    open()

    # create pic
    """def screenshot():
        # screenshot
        os.system('adb shell screencap -p /sdcard/screentest.png') 
        # pull to latop
        os.system('adb pull /sdcard/screentest.png /home/hauying/Desktop/auto_python/call ')

    screenshot()
"""


    def home_screen():
        d.press.home()
        sleep(1)


    home_screen()

except:

    print("something went wrong please check your code")

else:
    print("calling went done please check file")
    x = input("輸入 0 run\n 1 exit :")
    x = int(x)

    if x == 0:
        print("run gmail")


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
            ##d(text="GOT IT").click()
            ##sleep(3)
            ##d(text="TAKE ME TO GMAIL").click()
            ##d(text="Next").click()
            ##d(text="OK").click()
            d(resourceId="com.google.android.gm:id/compose_button").click()
            sleep(1)
            ##d(text="Got it").click
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
            d.click(890.0, 140.0)
            sleep(2)


        open()


        # create pic
        def screenshot():
            # screenshot
            os.system('adb shell screencap -p /sdcard/screentest.png')
            # pull to latop
            os.system('adb pull /sdcard/screentest.png /home/hauying/Desktop/auto_python/gmail ')


        screenshot()
        print("Gmail done please check file")
    else:
        print("not run gmail")




