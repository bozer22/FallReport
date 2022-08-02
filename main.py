from selenium import webdriver
import pytest

path = "/Users/beyza.ozer/Downloads/chromedriver/chromedriver.exe"
web = "https://www.rtasks.net/Users/Login"
USER_NAME = "Beyza.Ozer"
PASSWORD = "Bebeklerim1!"

# 1.step Launch browser
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.maximize_window()
# 2. Navigate to URL 'http://rtask.net'
driver.get(web)
driver.implicitly_wait(10)
driver.maximize_window()
# 3. Verify that home page is visible successfully
# 4. Click on 'Username' button and #5. Enter a valid username
Username_button = driver.find_element_by_id("Username").send_keys(USER_NAME)

# 6. Click on 'Password' button and #7. Enter a valid password
Password_button = driver.find_element_by_id("Password").send_keys(PASSWORD)

# 8. Click 'Sign in' button
# finding the button using ID
signin_button = driver.find_element_by_xpath("//button[@type = 'submit']")
signin_button.click()
# 9. Verify that 'Invalid username or password. If you forgot your password, please contact your supervisor to reset

expected_title = "Login Report"
actual_title = driver.find_element_by_xpath("//div[@class = 'ui header']").is_displayed()
pytest.assertEquals(expected_title, driver.gettitle());
driver.find_element_by_id("Username").send_keys(USER_NAME)


#6. Click on 'Password' button and #7. Enter a valid password
Password_button = driver.find_element_by_id("Password").send_keys(PASSWORD)

#8. Click 'Sign in' button
# finding the button using ID
signin_button = driver.find_element_by_xpath("//button[@type = 'submit']")
signin_button.click()
#9. Verify that 'Invalid username or password. If you forgot your password, please contact your supervisor to reset

expected_title = "Login Report"
actual_title = driver.find_element_by_xpath("//div[@class = 'ui header']").is_displayed()
pytest.assertEquals(expected_title, driver.gettitle());