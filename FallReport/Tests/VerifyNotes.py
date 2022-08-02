from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
from random import randrange
from random import seed
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import date


executable_path = "C:/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
webPage = "https://www.rtasks.net/Users/Login"
USER_NAME = "Beyza.Ozer"
PASSWORD = "Bebeklerim1!"

class LoginTestRtasks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

        # Navigate to 'rtasks.net'
    def test_login_valid(self):
        self.driver.get(webPage)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # Login to 'rtasks.net'
        self.driver.find_element_by_id("Username").send_keys(USER_NAME)
        self.driver.find_element_by_id("Password").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        # Select 'test campus'
        self.driver.find_element_by_xpath("//span[@ng-bind='session.user.FullName']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@ui-sref='Campus']").click()
        self.driver.find_element_by_xpath("//select[@id='campus']").click()
        self.driver.find_element_by_xpath("//option[@value='1']").click()
        self.driver.find_element_by_xpath("//a[@class='ui huge fluid primary button']").click()
        # Click resident button
        self.driver.find_element_by_xpath("//a[@ui-sref='Residents']").click()
        time.sleep(5)

        names1 = self.driver.find_elements_by_class_name("ng-binding")
        names2 = []

        for i in names1:
            names2.append(i.text)
        namess = names2[20:-1]
        names = namess[::4]
        num = randrange(3)
        print(num)
        nam = names[num]
        nem = nam[:9]
        print(nem)

        # if (num > 20)
        #     else
        #     self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        #     time.sleep(10)


        time.sleep(10)
        self.driver.find_element_by_xpath(f"//strong[contains(text(),  '{nem}')]").click()
        time.sleep(10)
        # Scroll down
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(10)

        # Click Notes
        self.driver.find_element_by_xpath("(//div[@class='content ng-scope'])[7]").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        # verify to see electronically by Beyza Ozer and time stamp
        time.sleep(10)
        #var = self.driver.find_element_by_xpath("(//tr[@ng-repeat])").text()
        #print(var)
        report = datetime.strptime((self.driver.find_element_by_xpath("(//div[@class='ng-binding'])[2]").text)[-26:-16], '%Y-%m-%d')
        print(report)
        print(type(report))
        report1 = str(report)
        report2 = report1[:-8]
        print(report2)
        # datetime.strptime
        today = str(date.today())
        print(today)
        print(type(today))
        print(type(report2))
        if today == report2:
            print('Test passed because the last report was today')
        else:
            print('Test failed because the last report was NOT today')








