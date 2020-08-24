from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME,'proceed').click()
wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()