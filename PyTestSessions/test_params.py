import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import xlrd

l = []
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    global l
    pass
class Test_facebooklogin(BaseTest):
    @pytest.mark.parametrize("username,pwd",l)
    def test_fbLoign(self,username,pwd):
        self.driver.get('https://twitter.com/LOGIN')
        #user = self.driver.find_element(By.XPATH,"//input[@name='session[username_or_email]']")
        wait = WebDriverWait(self.driver, 10)
        user = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@name='session[username_or_email]']")))
        user.send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@name='session[password]']").send_keys(pwd)
        print(self.driver.title)
def Datavalues():
    global l
    wb = xlrd.open_workbook("C:\Selenium_Python\SelPackage\ReadData.xlsx")
    sh = wb.sheet_by_name("Login")
    rcount=sh.nrows
    t=()
    l.clear()

    for x in range(1,rcount):
        username = sh.cell_value(x,0)
        pwd =sh.cell_value(x,1)
        t=(username,pwd)
        l.append(t)
    print(l)
    return l
Datavalues()
