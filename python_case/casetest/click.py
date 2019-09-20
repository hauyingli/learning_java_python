
from uiautomator import device as d



print(d.info)
d.screen.on()
d(text="Clock").click()


# d.screenshot("home.png")
# b.screenshot("123.png")
# # from uiautomator import device as d
# d(text="Clock").click()