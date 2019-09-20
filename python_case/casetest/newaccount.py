# Python3.6.4
# * coding:utf 8 *
# from uiautomator import device as d
from time import sleep
from uiautomator import device as d
import time
t = time.strftime("%Y%m%S",time.localtime())
print("t"+t)


# now = datetime.date.today ()
# name = "date {}"
# name_time = name.format (now)
# print (name_time)
def creatnew():
    d(text="Start").click()
    d(text="Skip").click()
    d(text="See all Wi‑Fi networks").click()
    sleep(1)
    d(text="GoogleGuest").click()
    sleep(60)
    d(text="Don’t copy").click()
    sleep(2)
    d(text="Create account").click()
    sleep(2)
    d(text="For myself").click()
    sleep(2)
    d.click(206.0, 653.0)
    sleep(1)
    d(resourceId="firstName").set_text("AlwaysTwoFiveTwoThree")
    d.press.enter()
    d(resourceId="lastName").set_text("PassNineFourThreeNine")
    d.press.enter()
    sleep(1)
    print("m")
    sleep(2)
    d(text="Month").click()
    sleep(2)
    print("done")
    sleep(2)
    d(text="April").click()
    print("2")
    sleep(1)
    d(resourceId="day").set_text("22")
    sleep(1)
    d(resourceId="year").set_text("1995")
    sleep(1)
    d(resourceId="gender").click()
    sleep(1)
    d(text="Female").click()
    sleep(2)
    d(text="Next").click()
    sleep(1)
    d(className="android.view.View") \
        .child(className="android.widget.EditText").set_text("t"+t)
    sleep(1)
    d(text="Next").click()
    sleep(1)
    d(className="android.view.View", resourceId="passwd") \
        .child(className="android.widget.EditText").set_text("sstsst1234")
    sleep(1)
    d(className="android.view.View", resourceId="confirm-passwd") \
        .child(className="android.widget.EditText").set_text("sstsst1234")
    d(text="Next").click()
    d(text="Next").click()
    d(resourceId="com.google.android.gms:id/suc_layout_status").swipe.up()
    d(resourceId="com.google.android.gms:id/suc_layout_status").swipe.up()
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
    d(text="More").click()
    d(text="Turn on").click()
    d(text="Skip").click()
    d(text="Do it later").click()
    d(text="Skip").click()
    d(text="Turn on").click()
    d(text="No thanks").click()
    sleep(2)
    d(text="Next").click()
    sleep(1)

creatnew()




























