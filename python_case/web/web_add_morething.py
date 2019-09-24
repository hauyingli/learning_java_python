from selenium import webdriver
import unittest
import HtmlTestRunner


class googlesearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../other/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("1")

    def test_search_1(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("automation step by step")
        # input "xx" in search bar
        self.driver.find_element_by_name("btnK").click()
        # cilck search button
        print("2")

    def test_search_howard(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("howard")
        # input "xx" in search bar
        self.driver.find_element_by_name("btnK").click()
        # cilck search button
        print("3")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("done")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/hauying/Desktop/github/webresult"))






