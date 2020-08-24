from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.w3schools.com/html/html_tables.asp')
tRows = len(driver.find_elements(By.XPATH, '//table[@id="customers"]/tbody/tr'))
tCols = len(driver.find_elements(By.XPATH, '//table[@id="customers"]/tbody/tr[1]/th'))
print(tRows)
print(tCols)
for r in range(1,tRows+1):
    for col in range(1,tCols+1):
        if r==1:
            val = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/th["+str(col)+"]").text
            print(val, end="    ")

        else:
            val = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(col)+"]").text
            print(val, end="    ")
    print()

