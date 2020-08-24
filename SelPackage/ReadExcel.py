import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
wb = xlrd.open_workbook("ReadData.xlsx")
sh = wb.sheet_by_name("Login")
rowCount = sh.nrows
colCount=sh.ncols
print(rowCount)
print(colCount)
for cur_row in range(1,rowCount):
    username = sh.cell_value(cur_row,0)
    pwd = sh.cell_value(cur_row,1)
    print(username, pwd)