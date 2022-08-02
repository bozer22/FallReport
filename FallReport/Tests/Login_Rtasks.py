from selenium import webdriver
import unittest

executable_path = "C:/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
webPage = "https://www.rtasks.net/Users/Login"
USER_NAME = "Beyza.Ozer"
PASSWORD = "Bebeklerim1!"

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        self.driver.get(webPage)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_id("Username").send_keys(USER_NAME)
        self.driver.find_element_by_id("Password").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        self.driver.find_element_by_xpath("//span[@ng-bind='session.user.FullName']").click()
        self.driver.find_element_by_xpath("//a[@ng-click='logout()']").click()


        #self.driver.close()
        #self.driver.quit()
        #print('Test completed!')