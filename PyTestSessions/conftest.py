import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["Chrome","Firefox"],scope='class')
def init_driver(request):
    print('-------------------------setup--------------------')
    if request.param=='Chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'Firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print('-------------------------Teardown--------------------')
    driver.quit()