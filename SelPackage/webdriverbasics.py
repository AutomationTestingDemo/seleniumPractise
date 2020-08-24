from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\KaLyAn\\Documents\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.google.com/')
print(driver.title)
driver.find_element(By.NAME,'q').send_keys('naveen automationlabs')
#time.sleep(5)
driver.implicitly_wait(5)
optionslist = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li')
print(len(optionslist))
for ele in optionslist:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break
print(driver.title)
#driver.quit()