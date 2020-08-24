import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= None
def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://google.com')
def teardown_module(module):
    driver.quit()
def test_googleTitle():
    assert driver.title =="Google", "Title Passed"
def test_googleUrl():
    assert driver.current_url == 'Hello Google'