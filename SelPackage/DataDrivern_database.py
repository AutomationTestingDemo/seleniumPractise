import cx_Oracle
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://milonic.com/login.php")
cn = cx_Oracle.connect("","","localhost/name")
cr = cn.cursor()
query="select * from employees"
cr.execute(query)
for cols in cr:
    driver.find_element_by_name("username").send_keys(cols[0])
    driver.find_element_by_name("password").send_keys(cols[1])
    driver.find_element_by_name("login").click()
    assert driver.title=="expected value",'This test is passed'
cr.close()
cn.close()
print("Test completed")
