from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('http://demo.automationtesting.in/Windows.html')
#driver.find_element(By.XPATH,"//a[@target='_blank']").click()
#driver.find_element(By.LINK_TEXT,'Open New Seperate Windows').click()
driver.find_element(By.LINK_TEXT,'Open Seperate Multiple Windows').click()
driver.find_element(By.XPATH,"//button[@onclick='multiwindow()']").click()
print(driver.current_window_handle)
handles= driver.window_handles
print(len(handles))
for handle in handles:
    print(handle)
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="":
        print("This window is empty so closing")
        driver.close()
