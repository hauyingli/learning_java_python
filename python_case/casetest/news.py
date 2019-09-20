# Python3.6.4
# * coding:utf 8 *
# from uiautomator import device as d
from time import sleep
from uiautomator import Device
import os
d = Device('8BLAY00DP1')
d = Device('8C3AX00FS5	')

def sss():
    d(text="Start").click()
    d(text="Skip").click()
    d(text="See all Wi‑Fi networks").click()
    sleep(1)
    d(text="GoogleGuest").click()
    sleep(60)
    d(text="Don’t copy").click()
    sleep(2)
    # d.click(193.0, 994.0)
    d (text="Create account").click()
    sleep(2)
    d(text="For myself").click()
    sleep(2)
    d.click(206.0, 653.0)
    sleep(1)
    d(resourceId="firstName").set_text("AlwaysTwoFiveTwoThree")
    d.press.enter()
    d(resourceId="lastName").set_text("NineFourThreeNine")
    d.press.enter()
    sleep(1)
    # d(text="Month").click
    d(resourceId="month").click
    # d.click(201.0, 650.0)取消
    sleep(1)
    # d.click(201.0, 650.0) #month取消
    d(text="April").click
    sleep(1)
    d(resourceId="day").set_text("22")
    sleep(1)
    d(resourceId="year").set_text("1995")
    sleep(1)
    # d(text="Gender").click
    d(resourceId="gender").click
    # d.click(332.0, 843.0)取消
    sleep(1)
    # d.click(332.0, 843.0)取消
    d(text="Female").click
    sleep(2)
    d.click(489.0, 1430.0)
    sleep(2)
    # d(resourceId="birthdaygenderNext").click#
    d(text="Next").click
    sleep(1)
    d(resourceId="birthdaygenderNext").click
    sleep(1)
    d(resourceId="identifierId").set_text("test0830good") #  Use  .time
    d(text="Next").click
    d(resourceId="passwd").set_text("sstsst1234")
    d(resourceId="confirm-passwd").set_text("sstsst1234")
    d(text="Next").click
    d(resourceId="com.google.android.gms:id/suc_layout_status").swipe.up()
    d(resourceId="com.google.android.gms:id/suc_layout_status").swipe.up()
    d(text="I agree").click
    d(text="Next").click
    sleep(30)
    d(text="More").click
    d(text="More").click
    d(text="Accept").click
    d(resourceId="com.android.settings:id/password_entry").set_text("0000")
    d(text="Next").click
    d(resourceId="com.android.settings:id/password_entry").set_text("0000")
    d(text="Confirm").click
    d(text="Skip").click
    d(text="Continue").click
    d(text="More").click
    d(text="Turn on").click
    d(text="Skip").click
    d(text="Do it later").click
    d(text="Skip").click
    d(text="Turn on").click
    d(text="No thanks").click
    sleep(2)
    d(text="Next").click
    sleep(1)

sss()











    
















