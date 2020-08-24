from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
options=options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.find_element(By.NAME,'upfile').send_keys('E:\Kalyan\Python Automation\Programs\strev.py')
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#To handle authentication popups
#driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')

#Downloading files also can be done by finding the download webelement and cliking on it
#to download the file in desired path use below code
# options.add_experimental_option("prefs",{"download.default_directory":"download path"})