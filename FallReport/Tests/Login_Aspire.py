from selenium import webdriver
import unittest
import time

executable_path = "C:/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
webPage = "https://app.aspireci.com/"
USER_NAME = "beyza.ozer@aspireci.com"
PASSWORD = "Bebeklerim1!"

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        #Login
        self.driver.get(webPage)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(USER_NAME)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        time.sleep(5)

        # Logout and close the window
        self.driver.find_element_by_xpath("(//button[@id='dropdownuser'])[1]").click()
        self.driver.find_element_by_xpath("(//button[@class='dropdown-item'])[1]").click()

        self.driver.close()
        self.driver.quit()
        print('Test completed!')