from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
# options =webdriver.ChromeOptions()
# options.add_argument("--allow-running-insecure-content")
# options.add_argument("--ignore-certificate-errors")
desiredcapabilities =DesiredCapabilities().CHROME.copy()
desiredcapabilities['acceptInsecureCerts']= True
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desiredcapabilities)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://expired.badssl.com/')
print(driver.find_element(By.TAG_NAME,'h1').text)