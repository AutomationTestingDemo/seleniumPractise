import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(params=["Chrome","Firefox"],scope='class')
# def init_driver(request):
#     print('-------------------------setup--------------------')
#     if request.param=='Chrome':
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == 'Firefox':
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = driver
#     yield
#     print('-------------------------Teardown--------------------')
#     driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_google_chrome(BaseTest):
    def test_GoogleTitle_chrome(self):
        self.driver.get('https://google.com')
        assert self.driver.title == "Google"