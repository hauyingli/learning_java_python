from uiautomator import device as d
from time import sleep
import os


def screen():
    d(resourceId="com.google.android.apps.nexuslauncher:id/scrim_view").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(className="android.widget.LinearLayout").swipe.down()
    sleep(1)
    d(resourceId="android:id/edit").click()
    sleep(1)
    d(resourceId="android:id/list").swipe.up()
    sleep(1)
    d(resourceId="android:id/list").swipe.up()
    sleep(1)
    d(text="Location").drag_to(561, 1236)
    # d.drag(203, 1523, 561, 1239) # Drag for 0.5s(default)
    # sleep(1)
    # d(resourceId="android:id/list").swipe.up()
    # sleep(1)
    # d.drag(203, 1523, 561, 1239)
    # sleep(1)
    # d(resourceId="android:id/list").swipe.up()
    # sleep(1)
    # d.drag(203, 1523, 561, 1239)
screen()