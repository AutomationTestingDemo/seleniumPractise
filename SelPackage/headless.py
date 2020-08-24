from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
options = webdriver.ChromeOptions()
options.headless=False
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(20)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
print(driver.title)