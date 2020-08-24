from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
options = webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(20)
driver.get('https://www.amazon.in/')
print(driver.title)
driver.get_screenshot_as_file('Amazon.png')#works for only .png
driver.save_screenshot("path and file.exection where u want to save the screenshot")#works for .jpg and .png
#to get screenshot of full page use below code
s= lambda x : driver.execute_script('return document.body.parentNode.scroll'+x)
driver.set_window_size(s('Width'),s('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('Full Amazon.png')
