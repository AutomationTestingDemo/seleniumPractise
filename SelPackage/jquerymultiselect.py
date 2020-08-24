from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
def multiselect(opitonsList, selectList):
    for l in selectList:
        for m in opitonsList:
            if m.text==l:
                m.click()
                break

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
print(driver.title)
driver.find_element(By.ID,'justAnInputBox').click()
list = driver.find_elements(By.XPATH,"//span[@class='comboTreeItemTitle']")
for l in list:
    if l is not None:
        print(l.text)
l1 = ['choice 1','choice 2 1','choice 5','choice 6 1','choice 6 2 3','choice 7']
multiselect(list,l1)
l1 = ['choice 2','choice 5','choice 6 1','choice 6 2','choice 7']
driver.find_element(By.ID,'justAnInputBox1').click()
list = driver.find_elements(By.XPATH,"//span[@class='comboTreeItemTitle']")
multiselect(list,l1)
driver.find_element(By.ID,'justAnotherInputBox').click()
list = driver.find_elements(By.XPATH,"//span[@class='comboTreeItemTitle']")
l1=['choice 2 3']
multiselect(list,l1)
