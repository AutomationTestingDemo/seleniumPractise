from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#browserName = 'chrome'
browserName = input("Enter the browserName :")

if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == 'safari':
    driver = webdriver.Safari()
else :
    print('Please pass the correct browsername, entered one is :'+ browserName)
    raise Exception('Driver not found')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.udemy.com/')
print(driver.title)


