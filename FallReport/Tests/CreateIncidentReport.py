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
executable_path = "C:/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
webPage2 = "https://app.aspireci.com/"
USER_NAME2 = "beyza.ozer@aspireci.com"
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
        num = randrange(1)
        print(num)
        nam = names[num]

        # Select 'test campus'
        self.driver.find_element_by_xpath("//span[@ng-bind='session.user.FullName']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@ui-sref='Campus']").click()
        self.driver.find_element_by_xpath("//select[@id='campus']").click()
        self.driver.find_element_by_xpath("//option[@value='1']").click()
        self.driver.find_element_by_xpath("//a[@class='ui huge fluid primary button']").click()
        self.driver.find_element_by_xpath("//a[@href='javascript:void(0)']").click()
        self.driver.find_element_by_xpath("(//a[@class='ng-scope'])[4]").click()
        self.driver.find_element_by_xpath("//a[@ui-sref='Incident']").click()
        # report incident
        self.driver.find_element_by_xpath("//a[@data-ui-sref='ReportIncident']").click()
        # enter date,time,category,type,resident
        self.driver.find_element_by_id("date").send_keys("07/14/2022")
        self.driver.find_element_by_id("time").send_keys("8:00 PM")
        time.sleep(3)
        self.driver.find_element_by_name("category").send_keys("Incident-Resident")
        time.sleep(3)
        self.driver.find_element_by_name("type").send_keys("Fall")
        self.driver.find_element_by_name("resident").send_keys(nam)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(15)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Location of fall’ ‘Living room’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[1]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.find_element_by_xpath("(//a[@ng-click='setText(option, record)'])[2]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘What is/was the position of the resident?’ ‘front’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[2]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[9]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(3)


        # Select ‘Assistive device utilized by resident:’ ‘Cane’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[3]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[13]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Footwear at time of incident was:’ ‘slippers’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[4]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[19]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘What is/was the surrounding area like?’ ‘busy’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[5]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[29]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘What is/was the floor like?’ ‘uneven’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[6]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[37]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘What was the resident doing just before the fall?’ send answer ‘walking’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[7]").send_keys("Walking")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘What was the resident trying to do? What was different this time?’ ‘none’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[8]").send_keys("None")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Did the resident have glasses and/or hearing aids on?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[9]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Did the resident have glasses and/or hearing aids on?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[10]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Brief Narrative of the incident’ send answer ‘none’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[11]").send_keys("None")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Nurse Notified’ ‘yes’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[12]").send_keys("Yes")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Was the resident sent to the ER as a result of the fall? If yes, why?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[13]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        time.sleep(5)
        # Click ‘Submit’
        self.driver.find_element_by_xpath("//button[@type ='submit']").click()
        time.sleep(5)
        # self.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)

        # View the vitals page and click 'temp' text box
        self.driver.find_element_by_xpath("(//input[@id='serviceValue'])[12]").send_keys('100')
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # click 'time spent' send keys '30'
        self.driver.find_element_by_xpath("(//input[@name='minutes'])").send_keys('30')
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click 'save'
        self.driver.find_element_by_xpath("//button[@type ='submit']").click()


'''from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import unittest
import time
from selenium.webdriver.common.keys import Keys


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

#Navigate to 'rtasks.net'
    def test_login_valid(self):
        self.driver.get(webPage)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
#Login to 'rtasks.net'
        self.driver.find_element_by_id("Username").send_keys(USER_NAME)
        self.driver.find_element_by_id("Password").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
#Select 'test campus'
        self.driver.find_element_by_xpath("//span[@ng-bind='session.user.FullName']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@ui-sref='Campus']").click()
        self.driver.find_element_by_xpath("//select[@id='campus']").click()
        self.driver.find_element_by_xpath("//option[@value='1']").click()
        self.driver.find_element_by_xpath("//a[@class='ui huge fluid primary button']").click()
        self.driver.find_element_by_xpath("//a[@href='javascript:void(0)']").click()
        self.driver.find_element_by_xpath("(//a[@class='ng-scope'])[4]").click()
        self.driver.find_element_by_xpath("//a[@ui-sref='Incident']").click()
        #report incident
        self.driver.find_element_by_xpath("//a[@data-ui-sref='ReportIncident']").click()
        #enter date,time,category,type,resident
        self.driver.find_element_by_id("date").send_keys("07/14/2022")
        self.driver.find_element_by_id("time").send_keys("8:00 PM")
        time.sleep(3)
        self.driver.find_element_by_name("category").send_keys("Incident-Resident")
        time.sleep(3)
        self.driver.find_element_by_name("type").send_keys("Fall")
        self.driver.find_element_by_name("resident").send_keys("Armenta,Karina")
        time.sleep(12)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Location of fall’ ‘Living room’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[1]").click()
        self.driver.find_element_by_xpath("(//a[@ng-click='setText(option, record)'])[2]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        #Select ‘What is/was the position of the resident?’ ‘front’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[2]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[9]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Assistive device utilized by resident:’ ‘Cane’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[3]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[13]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Footwear at time of incident was:’ ‘slippers’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[4]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[19]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘What is/was the surrounding area like?’ ‘busy’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[5]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[29]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘What is/was the floor like?’ ‘uneven’
        self.driver.find_element_by_xpath("(//a[@ng-show='record.Options'])[6]").click()
        self.driver.find_element_by_xpath("(//a[@class='snippet-link ng-binding'])[37]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘What was the resident doing just before the fall?’ send answer ‘walking’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[7]").send_keys("Walking")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘What was the resident trying to do? What was different this time?’ ‘none’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[8]").send_keys("None")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Did the resident have glasses and/or hearing aids on?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[9]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Select ‘Did the resident have glasses and/or hearing aids on?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[10]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Brief Narrative of the incident’ send answer ‘none’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[11]").send_keys("None")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Nurse Notified’ ‘yes’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[12]").send_keys("Yes")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click ‘Was the resident sent to the ER as a result of the fall? If yes, why?’ ‘No’
        self.driver.find_element_by_xpath("(//textarea[@ng-model='record.Answer'])[13]").send_keys("No")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(5)
        # Click ‘Submit’
        self.driver.find_element_by_xpath("//button[@type ='submit']").click()
        time.sleep(5)
        #self.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        #View the vitals page and click 'temp' text box
        self.driver.find_element_by_xpath("(//input[@id='serviceValue'])[12]").send_keys('100')
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        #click 'time spent' send keys '30'
        self.driver.find_element_by_xpath("(//input[@name='minutes'])").send_keys('30')
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        #Click 'save'
        self.driver.find_element_by_xpath("//button[@type ='submit']").click()'''



