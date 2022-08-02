from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import unittest
import time
from selenium.webdriver.common.keys import Keys

executable_path = "C:/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
webPage2 = "https://app.aspireci.com/"
USER_NAME2 = "beyza.ozer@aspireci.com"
PASSWORD = "Bebeklerim1!"


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    # Navigate to 'https://app.aspireci.com/'
    def test_login_valid(self):
        # Login
        self.driver.get(webPage2)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(USER_NAME2)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
        time.sleep(2)
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
        time.sleep(1)

        # Click 'pulse' textbox, send '100'
        self.driver.find_element_by_id("eventPulse").send_keys("100")
        time.sleep(1)

        # Click 'respiration' textbox, send '100'
        self.driver.find_element_by_id("eventRespiration").send_keys("100")
        time.sleep(1)

        # Click 'blood pressure' textbox, send '100'
        self.driver.find_element_by_id("eventBP").send_keys("100")
        time.sleep(1)

        # Click 'MAHC 10 Score"' textbox, send '100'(
        self.driver.find_element_by_id("MAHC10Score").send_keys("100")
        time.sleep(1)

        self.driver.find_element_by_id("MAHC10ScoreDate").send_keys("07152022")
        time.sleep(1)

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
