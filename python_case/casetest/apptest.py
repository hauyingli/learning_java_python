import unittest
import time
##from appium import webdriver
from uiautomator import Device


class WhatsappAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platfromName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 3a XL'
        desired_caps['noReset'] = 'ture'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'

        self.driver = webdriver.Remote('http;//localhost;4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")
        search_button.click()

        name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
        name_search_box.send_keys("Anna")

        msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Anna")')
        msg.click()

        text_box = self.driver.find_element_by_id("com.whatsapp:id/entry")
        text_box.send_keys("Testing....")

        send_button = self.driver.find_element_by_id("com.whatsapp:id/send")
        send_button.click()

        time.sleep(10)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
