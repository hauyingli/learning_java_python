# Python3.6.4
# * coding:utf 8 *
# from uiautomator import device as d
from time import sleep
from uiautomator import Device
import time
import account as a
print("Run " + a.acc + " account")
d = Device('8B9AY009XF')
c = Device('8BDAX00AJL')
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
    # d(className="android.widget.EditText").set_text(a.acc)
    sleep(1)
    d(text="Next").click()
    sleep(2)
    d(className="android.widget.EditText").set_text(a.pw)
    sleep(1)
    d(text="Next").click()
    sleep(1)
    # d(text="I agree").click()
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
def Q2():
    c(text="Start").click()
    c(text="Skip").click()
    c(text="See all Wi‑Fi networks").click()
    sleep(1)
    c(text="GoogleGuest").click()
    sleep(60)
    c(text="Don’t copy").click()
    sleep(2)
    c(resourceId="identifierId").set_text(a.acc)
    # d(className="android.widget.EditText").set_text(a.acc)
    sleep(1)
    c(text="Next").click()
    sleep(2)
    c(className="android.widget.EditText").set_text(a.pw)
    sleep(1)
    c(text="Next").click()
    sleep(1)
    # d(text="I agree").click()
    sleep(30)
    c(text="More").click()
    c(text="More").click()
    c(text="Accept").click()
    c(resourceId="com.android.settings:id/password_entry").set_text("0000")
    c(text="Next").click()
    c(resourceId="com.android.settings:id/password_entry").set_text("0000")
    c(text="Confirm").click()
    c(text="Skip").click()
    c(text="Continue").click()
    c(text="I agree").click()
    c(text="Next").click()
    c(text="Do it later").click()
    c(text="Skip").click()
    c(text="Turn on").click()
    c(text="No thanks").click()
    sleep(2)
    c(text="Next").click()
    sleep(1)

Q2()




























