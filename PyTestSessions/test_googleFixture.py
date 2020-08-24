import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('-------------------------setup--------------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://google.com')

    yield
    print('-------------------------Teardown--------------------')
    driver.quit()

# @pytest.mark.usefixtures("init_driver")
# def test_googleTitle():
#     assert driver.title =="Google", "Title Passed"
#above format also can be used if dont want to pass fixture name as argument to the method

def test_googleTitle(init_driver):
    assert driver.title =="Google", "Title Passed"
def test_googleUrl(init_driver):
    assert driver.current_url == 'https://www.google.com/'