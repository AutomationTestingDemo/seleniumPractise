from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
option.add_argument("no-sandbox")
option.add_argument("--disable-gpu")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.amazon.in/')
# driver.add_cookie({"name":"dhanya","domain":"reddit.com","value":"pussyAndass"})
cookies  = driver.get_cookies()
print(len(cookies))
for cookie in cookies:
    print(cookie)

# driver.delete_cookie("name of the cookie")