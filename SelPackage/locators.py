from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
print(driver.title)
usernameurl = driver.find_element(By.ID,'Form_submitForm_subdomain')
firstname = driver.find_element(By.NAME,'FirstName')
lastname = driver.find_element(By.XPATH,"//input[@placeholder ='Last Name']")
email = driver.find_element(By.ID,'Form_submitForm_Email')
features_link = driver.find_element(By.LINK_TEXT,'Features')
#jobtitle = driver.find_element(By.ID,'Form_submitForm_JobTitle')
#numberOfEmp = driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
#companyname = driver.find_element(By.ID,'Form_submitForm_CompanyName')
industry = driver.find_element(By.ID,'Form_submitForm_Industry')
#phone = driver.find_element(By.ID,'Form_submitForm_Contact')
country = driver.find_element(By.ID,'Form_submitForm_Country')
#checkbox = driver.find_element(By.CLASS_NAME,'checkbox')
#captcha = driver.find_element(By.CLASS_NAME,'recaptcha-checkbox-border')
#submit = driver.find_element(By.ID,'Form_submitForm_action_request')
usernameurl.send_keys("k028941")
firstname.send_keys('Kalyan')
lastname.send_keys('Mundra')
email.send_keys('Kalyan.mundra@capgemini.com')
select = Select(industry)
select.select_by_value("Travel")
select2 = Select(country)
select2.select_by_visible_text('Austria')
for c in select.options:
    print(c.text)
    if c.text == "Education":
        c.click()
        break



#header =  driver.find_element(By.TAG_NAME,'h5')
#print(header.text)
#linksList = driver.find_elements(By.TAG_NAME,'a')
#print(len(linksList))
#for link in linksList:
#    if link.get_attribute('href') is not None:
#        print(link.get_attribute('href'),' ',link.text)
#features_link.click()
#print(driver.title)
