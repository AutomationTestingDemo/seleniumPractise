import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='class')
def init_Chromedriver(request):
    print('-------------------------setup--------------------')
    Chdriver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = Chdriver
    yield
    print('-------------------------Teardown--------------------')
    Chdriver.quit()

@pytest.fixture(scope='class')
def init_Firefoxdriver(request):
    print('-------------------------setup--------------------')
    FFdriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = FFdriver
    yield
    print('-------------------------Teardown--------------------')
    FFdriver.quit()

@pytest.mark.usefixtures("init_Chromedriver")
class Base_Google_Chrome:
    pass
class Test_google_chrome(Base_Google_Chrome):
    def test_GoogleTitle_chrome(self):
        self.driver.get('https://google.com')
        assert self.driver.title == "Google"

@pytest.mark.usefixtures("init_Firefoxdriver")
class Base_Google_FireFox:
    pass
class Test_google_firefox(Base_Google_FireFox):
    def test_GoogleTitle_firefox(self):
        self.driver.get('https://google.com')
        assert self.driver.title == "Google"
