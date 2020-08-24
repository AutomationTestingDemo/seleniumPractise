from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.google.com/')
    print(driver.title)
def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.facebook.com/')
    print(driver.title)
def test_youtube():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.youtube.com/')
    print(driver.title)
def test_prime():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.primevideo.com/')
    print(driver.title)
test_google()
test_facebook()
test_youtube()
test_prime()