from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('http://www.londonfreelance.org/courses/frames/index.html')
frames = driver.find_elements(By.TAG_NAME,'frame')
list =[]
print(len(frames))
for f in frames:
    print(f.get_attribute('src'))
    list.append(str(f.get_attribute('name')))
print(list)
for l in list:
    driver.switch_to.frame(l)
    print('header string is :',driver.find_element(By.XPATH,'/html/body').text)
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()