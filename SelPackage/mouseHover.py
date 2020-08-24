from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.spicejet.com/')
print(driver.title)
loginbutton = driver.find_element(By.ID,'highlight-addons')
action = ActionChains(driver)
action.move_to_element(loginbutton).perform()
driver.find_element(By.XPATH,'//li[@id="header-addons"]/ul/li[3]/a').click()
#action.move_to_element(driver.find_element(By.XPATH,'//li[@id="header-addons"]/ul/li[3]/a')).perform().click()
print(driver.title)
