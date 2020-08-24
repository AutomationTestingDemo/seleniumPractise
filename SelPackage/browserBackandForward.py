from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.amazon.in/')
driver.find_element(By.LINK_TEXT,'Amazon Pay').click()
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.back()
print(driver.title)
driver.refresh()