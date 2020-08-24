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
driver.get('https://app.hubspot.com/login')
# pay = driver.find_element(By.LINK_TEXT,'Amazon Pay')
# driver.execute_script("arguments[0].click();",pay)
# title = driver.execute_script("return document.title;")
# print(title)
# driver.execute_script('history.go(0);')
# driver.execute_script("alert('Hello Selenium');")
# driver.switch_to.alert.accept()
# print(title)
# print(driver.execute_script("return document.documentElement.innerText;"))
# element = driver.find_element(By.XPATH,"//span[text()='Featured categories & brands']")
# driver.execute_script("arguments[0].scrollIntoView(true);",element)
# username =driver.find_element(By.ID,'username')
# driver.execute_script("arguments[0].value='chakri';",username)
driver.execute_script("document.getElementById('username').value='Kalyan'")
