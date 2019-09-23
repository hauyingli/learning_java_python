# Python3.6.4
# * coding:utf 8 *
# from uiautomator import device as d
from time import sleep
from uiautomator import device as d
import time
import account as a
print("Run " + a.acc + " account")

def Qkseeting():
    d(text="Start").click()
    d(text="Skip").click()
    d(text="See all Wi‑Fi networks").click()
    sleep(1)
    d(text="GoogleGuest").click()
    sleep(60)
    d(text="Don’t copy").click()
    sleep(2)
    d(resourceId="identifierId").set_text(a.acc)
    sleep(1)
    d(text="Next").click()
    sleep(2)
    d(className="android.widget.EditText").set_text(a.pw)
    sleep(1)
    d(text="Next").click()
    sleep(1)
    d(text="I agree").click()
    sleep(30)
    d(text="More").click()
    d(text="More").click()
    d(text="Accept").click()
    d(resourceId="com.android.settings:id/password_entry").set_text("0000")
    d(text="Next").click()
    d(resourceId="com.android.settings:id/password_entry").set_text("0000")
    d(text="Confirm").click()
    d(text="Skip").click()
    d(text="Continue").click()
    d(text="I agree").click()
    d(text="Next").click()
    d(text="Do it later").click()
    d(text="Skip").click()
    d(text="Turn on").click()
    d(text="No thanks").click()
    sleep(2)
    d(text="Next").click()
    sleep(1)

Qkseeting()




























