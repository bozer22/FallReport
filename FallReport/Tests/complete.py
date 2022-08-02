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
        num = randrange(len(names))
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

        # Select ‘What is/was the position of the resident?’ ‘front’
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

        # Wait for 10 minutes to see the report on aspire website
        time.sleep(600)

    # Navigate to 'https://app.aspireci.com/'
        self.driver
        self.driver.get(webPage2)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(USER_NAME2)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        time.sleep(5)

        # Click 'events' dropdown
        self.driver.find_element_by_xpath("(//span[@class='mr-1 dropdown-label'])[2]").click()
        time.sleep(2)

        # Click 'Fall' tab then scroll down
        self.driver.find_element_by_xpath("//a[@href='/events/falls']").click()
        time.sleep(45)

        # Experienced Injury? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[1]").click()
        time.sleep(1)

        # Actual or Suspected Head Involvement? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[2]").click()
        time.sleep(1)


        #EMS was Involved? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[3]").click()
        time.sleep(1)


        # Click 'temperature' textbox, send '100'
        self.driver.find_element_by_id("eventTemp").send_keys("100")
        time.sleep(2)

        # Click 'pulse' textbox, send '100'
        self.driver.find_element_by_id("eventPulse").send_keys("100")
        time.sleep(2)

        # Click 'respiration' textbox, send '100'
        self.driver.find_element_by_id("eventRespiration").send_keys("100")
        time.sleep(2)

        # Click 'blood pressure' textbox, send '100'
        self.driver.find_element_by_id("eventBP").send_keys("100")
        time.sleep(2)

        # Click 'MAHC 10 Score"' textbox, send '100'(
        self.driver.find_element_by_id("MAHC10Score").send_keys("100")
        time.sleep(2)

        self.driver.find_element_by_id("MAHC10ScoreDate").send_keys("07152022")
        time.sleep(2)

        # Click 'SLUMS Score"' textbox, send '100'
        self.driver.find_element_by_id("SLUMSScore").send_keys("100" + Keys.TAB + "07152022")
        time.sleep(2)

        #Scroll down
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click 'responsible party' check box
        self.driver.find_element_by_xpath("//input[@class='form-check-input'][1]").click()
        time.sleep(1)

        # Click 'name',send 'Beyza Ozer'+ date send '06/09/2022 04:55 AM'
        self.driver.find_element_by_xpath("//input[@id='responsiblePartyName']").send_keys("Beyza Ozer" + Keys.TAB + "07152022" + Keys.TAB + "0455A"
                                                                                           + Keys.TAB + Keys.SPACE + Keys.TAB +
                                                                                           "Beyza Ozer" + Keys.TAB + "07152022" + Keys.TAB + "0455A")

        time.sleep(2)

        # Click 'Primary Physician' check box
        # self.driver.find_element_by_xpath("(//input[@class='form-check-input'])[2]").click()

        # Click 'Primary Physician',send 'Beyza Ozer' + date send '06/09/2022 06:00 AM'
        # self.driver.find_element_by_id("//input[@id='physicianName']").send_keys("Beyza Ozer" + Keys.TAB + "06092022" + Keys.TAB + "0455A")

        # scroll down
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Does the resident have a diagnosis of hypertension? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[6]").click()
        time.sleep(1)

        # Is the resident on anti-hypertensive medication? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[7]").click()
        time.sleep(1)

        # Does the resident have a diagnosis of cardiac arrhythmia? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[8]").click()
        time.sleep(1)

        # Is the resident currently receiving anticoagulation therapy? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[9]").click()
        time.sleep(1)

        # Is the resident on home health services? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[10]").click()
        time.sleep(1)

        # Is the resident on hospice services? Yes   No
        self.driver.find_element_by_xpath("(//input[@value='no'])[11]").click()
        time.sleep(1)

        # Is the resident on outpatient services? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[12]").click()
        time.sleep(1)

        # The protocols have been entered on the resident's service plan/care plan. No
        self.driver.find_element_by_xpath("(//input[@value='no'])[13]").click()
        time.sleep(1)

        # Is the resident able to stand with or without assistance? yes
        self.driver.find_element_by_xpath("(//input[@value='yes'])[14]").click()
        time.sleep(1)

        # Does the resident have an active infection? No
        self.driver.find_element_by_xpath("(//input[@value='no'])[15]").click()
        time.sleep(1)

        # scroll down
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # click "close event and send nurse's note
        self.driver.find_element_by_xpath("//button[@id='note-submit']").click()

        # Navigate to 'rtasks.net'
        self.driver
        self.driver.get(webPage)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # Login to 'rtasks.net'
        # self.driver.find_element_by_id("Username").send_keys(USER_NAME)
        # self.driver.find_element_by_id("Password").send_keys(PASSWORD)
        # self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        # Select 'test campus'
        self.driver.find_element_by_xpath("//span[@ng-bind='session.user.FullName']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@ui-sref='Campus']").click()
        self.driver.find_element_by_xpath("//select[@id='campus']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//option[@value='1']").click()
        self.driver.find_element_by_xpath("//a[@class='ui huge fluid primary button']").click()
        # Click resident button
        self.driver.find_element_by_xpath("//a[@ui-sref='Residents']").click()
        time.sleep(5)



        ######
        # names1 = self.driver.find_elements_by_class_name("ng-binding")
        # names2 = []

        # for i in names1:
        #     names2.append(i.text)
        # namess = names2[20:-1]
        # names = namess[::4]
        # num = randrange(3)
        # print(num)
        # nam = names[num]
        # ####


        nem = nam[:9]
        print(nem)


        if 20 < num <= 40:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
        elif 40 < num <= 60:
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 1200)")



        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        #
        #
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
        # var = self.driver.find_element_by_xpath("(//tr[@ng-repeat])").text()
        # print(var)
        report = datetime.strptime((self.driver.find_element_by_xpath("(//div[@class='ng-binding'])[2]").text)[-26:-16],
                                   '%Y-%m-%d')
        print(report)
        print(type(report))
        report1 = str(report)
        report2 = report1[:-9]
        print(report2)
        # datetime.strptime
        today = str(date.today())
        print(today)
        print(type(today))
        print(type(report2))

        print(len(today))
        print(len(report2))
        if today == report2:
            print('Test passed because the last report was today')
        else:
            print('Test failed because the last report was NOT today')




        '''self.driver.find_element(by=By.XPATH, value="//a[@ui-sref='Residents']").click()
        time.sleep(5)

        names1 = self.driver.find_elements_by_class_name("ng-binding")
        names2 = []

        for i in names1:
            names2.append(i.text)
        namess = names2[20:-1]
        names = namess[::4]
        num = randrange(20)
        print(num)
        nam = names[num]
        nem = nam[:9]
        print(nem)

        # if (num > 20)
        #     else
        #     self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        #     time.sleep(10)


        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=f"//strong[contains(text(),  '{nem}')]").click()
        time.sleep(10)
        # Scroll down
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(10)

        # Click Notes
        self.driver.find_element(by=By.XPATH, value="(//div[@class='content ng-scope'])[7]").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        # verify to see electronically by Beyza Ozer and time stamp
        time.sleep(10)
        var = self.driver.find_element_by_xpath("(//tr[@ng-repeat])").text()
        print(var)'''


